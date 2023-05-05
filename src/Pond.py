import os.path as path
import random
import sys

import pygame
from PySide6.QtWidgets import QApplication
from ZombieFishSprite import ZombieFishSprite

import config
from Dashboard import Dashboard
from factories import fishFactory
from FishSchool import FishSchool
from FishSprite import FishSprite
from Log import get_logger
from LogHandler import LogHandler
from Storage import Storage
from vivisystem import (EventType, VivisystemClient, VivisystemFish,
                        VivisystemPond)

UPDATE_DATA_EVENT = pygame.USEREVENT + 1
PHEROMONE_EVENT = pygame.USEREVENT + 2
PHEROMONE_ACTIVE_EVENT = pygame.USEREVENT + 3
SEND_DATA_EVENT = pygame.USEREVENT + 4
ZOMBIE_EVENT = pygame.USEREVENT + 5

log = get_logger("pond")


class Pond:

    def __init__(self, name: str, storage: Storage = None, client: VivisystemClient = None):
        self.__name: str = name

        self.__storage: Storage = storage
        self.__client: VivisystemClient = client
        self.__connected_ponds = {}
        self.__fish_school = FishSchool()

        self.__pheromone_active = False
        self.__pheromone_timer_active = False

    def get_name(self):
        return self.__name

    def __load_fishes(self):
        fishes = self.__storage.get_fishes()
        if len(fishes) == 0:
            return
        for fish in fishes:
            self.__fish_school.add_fish(fish)
        log.info(f"Loaded {len(fishes)} fishes")

    def spawn_fish(self, genesis: str = None, parent_id: str = None):
        genesis = genesis if genesis else self.__name
        fish = fishFactory.generate_fish_sprite(genesis, parent_id)
        self.__fish_school.add_fish(fish)

        if self.__storage:
            self.__storage.add_fish(fish)
        log.info(f"Spawned fish {fish.get_id()}")

    def add_fish(self, fish: FishSprite):
        self.__fish_school.add_fish(fish)

    def remove_fish(self, fish: FishSprite):
        self.__fish_school.remove_fish(fish)

    def __update_fish(self, fish: FishSprite):
        if not fish.is_alive():
            self.__fish_school.remove_fish(fish)
        fish.update_data()

        if self.__pheromone_active:
            pheromone_value = random.randint(25, 50) * config.BIRTH_RATE
            fish.add_pheromone(pheromone_value)

        if fish.is_pregnant():
            self.spawn_fish(fish.get_genesis(), fish.get_id())
            fish.set_gave_birth(True)

        if self.__connected_ponds:
            if fish.get_genesis() != self.__name and fish.get_time_in_pond() >= 5 and not fish.get_gave_birth():
                self.spawn_fish(fish.get_genesis(), fish.get_id())
                fish.set_gave_birth(True)

            if fish.get_genesis() == self.__name and fish.get_time_in_pond() >= 15:
                random_pond = random.choice(
                    list(self.__connected_ponds.values()))
                self.__client.migrate_fish(
                    random_pond, fish.to_vivisystemFish())
                self.remove_fish(fish)

            if fish.get_crowd_threshold() < self.__fish_school.get_population():
                random_pond = random.choice(
                    list(self.__connected_ponds.values()))
                self.__client.migrate_fish(
                    random_pond, fish.to_vivisystemFish())
                self.remove_fish(fish)

    def handle_migrate(self, vivi_fish: VivisystemFish):
        fish = FishSprite.from_vivisystemFish(vivi_fish)
        self.add_fish(fish)
        log.info(
            f"Migrated fish {fish.get_id()} from {vivi_fish.genesis}")

    def handle_status(self, vivi_pond: VivisystemPond):
        self.__connected_ponds[vivi_pond.name] = vivi_pond

    def handle_disconnect(self, pond_name: str):
        if pond_name in self.__connected_ponds:
            del self.__connected_ponds[pond_name]
            log.info(f"{pond_name} disconnected")

    def shutdown(self):
        if self.__client:
            self.__client.disconnect()
        log.info("Shutting down")
        sys.exit()

    def run(self):
        pygame.init()
        pygame.display.set_caption(f"385dc-FishHaven [{self.__name}]")
        screen = pygame.display.set_mode(config.WINDOW_SIZE)
        background_path = path.join(config.ASSET_DIR, "background.jpg")
        background = pygame.image.load(background_path)
        background = background.convert()
        background = pygame.transform.scale(background, config.WINDOW_SIZE)
        clock = pygame.time.Clock()

        moving_sprites = pygame.sprite.Group()

        pygame.time.set_timer(UPDATE_DATA_EVENT, 1000)
        pygame.time.set_timer(PHEROMONE_EVENT, 15000)
        pygame.time.set_timer(ZOMBIE_EVENT, 20000)

        app = QApplication(sys.argv)
        dashboard = Dashboard(self.__fish_school)
        log.addHandler(LogHandler(dashboard))

        if self.__storage:
            self.__load_fishes()

        if self.__client:
            handler_map = {
                EventType.MIGRATE: self.handle_migrate,
                EventType.STATUS: self.handle_status,
                EventType.DISCONNECT: self.handle_disconnect
            }
            for event_type, handler in handler_map.items():
                self.__client.handle_event(event_type, handler)

        running = 1
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0

                if event.type == UPDATE_DATA_EVENT:
                    self.__fish_school.update_data(self.__update_fish)

                if event.type == PHEROMONE_EVENT:
                    log.info("Pheromon activated")
                    self.__pheromone_active = True

                    if not self.__pheromone_timer_active:
                        self.__pheromone_timer_active = True
                        pygame.time.set_timer(PHEROMONE_ACTIVE_EVENT, 3000)

                if event.type == PHEROMONE_ACTIVE_EVENT and self.__pheromone_active:
                    log.info("Pheromon deactivated")
                    self.__pheromone_active = False
                    self.__pheromone_timer_active = False
                    pygame.time.set_timer(PHEROMONE_EVENT, 15000)

                if event.type == SEND_DATA_EVENT:
                    self.__client.send_status(VivisystemPond(
                        self.name,
                        self.__fish_school.get_population(),
                        config.BIRTH_RATE))
                    
                if event.type == ZOMBIE_EVENT:
                    moving_sprites.add(ZombieFishSprite())
                    log.warning("Zombie fish spawned")

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        dashboard.show()

                    if config.DEBUG_MODE:
                        if event.key == pygame.K_a:
                            self.spawn_fish()

                        if event.key == pygame.K_s:
                            self.spawn_fish("test")

            for fish in self.__fish_school.sprites():
                for zombie in moving_sprites.sprites():
                    if pygame.sprite.collide_rect(fish, zombie):
                        self.__fish_school.remove_fish(fish)
                        fish.kill()
                        log.warning(f"Fish {fish.get_id()} eaten by zombie")
                

            self.__fish_school.update_sprite()
            moving_sprites.update()
            screen.blit(background, (0, 0))
            self.__fish_school.draw(screen)
            moving_sprites.draw(screen)
            pygame.display.flip()
            app.processEvents()

        pygame.quit()
        self.shutdown()


if __name__ == "__main__":
    pond = Pond(config.POND_NAME)
    pond.run()
