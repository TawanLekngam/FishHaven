import os.path as path
import random
import sys

import pygame
from PySide6.QtWidgets import QApplication

import config
from Dashboard import Dashboard
from factories import fishFactory
from FishSchool import FishSchool
from FishSprite import FishSprite
from Log import get_logger
from LogHandler import LogHandler
from PondData import PondData
from Storage import Storage


class Pond:
    UPDATE_DATA_EVENT = pygame.USEREVENT + 1
    PHEROMONE_EVENT = pygame.USEREVENT + 2
    PHEROMONE_ACTIVE_EVENT = pygame.USEREVENT + 3

    def __init__(self, name: str, storage: Storage = None):
        self.__name: str = name
        self.__data: PondData = PondData(name)
        self.__storage: Storage = storage
        self.__fish_school = FishSchool()
        self.__logger = get_logger("pond")
        self.__birth_rate = 0.15

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
        self.__logger.info(f"Loaded {len(fishes)} fishes")

    def spawn_fish(self, genesis: str = None, parent_id: str = None):
        genesis = genesis if genesis else self.__name
        fish = fishFactory.generate_fish_sprite(genesis, parent_id)
        self.__fish_school.add_fish(fish)
        self.__data.add_fish(fish.get_data())
        if self.__storage:
            self.__storage.add_fish(fish)
        self.__logger.info(f"Spawned fish {fish.get_id()}")

    def remove_fish(self, fish: FishSprite):
        self.__fish_school.remove_fish(fish)

    def __update_fish(self, fish: FishSprite):
        if not fish.is_alive():
            self.__fish_school.remove_fish(fish)
        fish.update_data()

        if self.__pheromone_active:
            pheromone_value = random.randint(25, 50) * self.__birth_rate
            fish.add_pheromone(pheromone_value)

        if fish.is_pregnant():
            self.spawn_fish(fish.get_genesis(), fish.get_id())

        if fish.get_time_in_pond() >= 15:
            # Todo: migrate fish
            ...

    def shutdown(self):
        self.__logger.info("Shutting down")

    def run(self):
        pygame.init()
        pygame.display.set_caption(f"385dc-FishHaven [{self.__name}]")
        screen = pygame.display.set_mode(config.WINDOW_SIZE)
        background_path = path.join(config.ASSET_DIR, "background.jpg")
        background = pygame.image.load(background_path)
        background = background.convert()
        background = pygame.transform.scale(background, config.WINDOW_SIZE)
        clock = pygame.time.Clock()

        pygame.time.set_timer(Pond.UPDATE_DATA_EVENT, 1000)
        pygame.time.set_timer(Pond.PHEROMONE_EVENT, 15000)

        app = QApplication(sys.argv)
        dashboard = Dashboard(self.__fish_school)
        self.__logger.addHandler(LogHandler(dashboard))

        if self.__storage:
            self.__load_fishes()

        running = 1
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0

                if event.type == Pond.UPDATE_DATA_EVENT:
                    self.__fish_school.update_data(self.__update_fish)

                if event.type == Pond.PHEROMONE_EVENT:
                    self.__logger.info("Injecting pheromone")
                    self.__pheromone_active = True

                    if not self.__pheromone_timer_active:
                        self.__pheromone_timer_active = True
                        pygame.time.set_timer(Pond.PHEROMONE_ACTIVE_EVENT, 3000)

                if event.type == Pond.PHEROMONE_ACTIVE_EVENT and self.__pheromone_active:
                    self.__logger.info("Pheromone expired")
                    self.__pheromone_active = False
                    self.__pheromone_timer_active = False
                    pygame.time.set_timer(Pond.PHEROMONE_EVENT, 15000)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        dashboard.show()

                    if config.DEBUG_MODE:
                        if event.key == pygame.K_a:
                            self.spawn_fish()

                        if event.key == pygame.K_s:
                            self.spawn_fish("test")

            self.__fish_school.update_sprite()
            screen.blit(background, (0, 0))
            self.__fish_school.draw(screen)
            pygame.display.flip()
            app.processEvents()

        pygame.quit()
        self.shutdown()
        sys.exit(0)


if __name__ == "__main__":
    pond = Pond(config.POND_NAME)
    pond.run()
