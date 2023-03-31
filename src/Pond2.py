import os.path as path

import pygame
import random

import config
from factories import fishFactory
from FishSchool import FishSchool
from FishSprite import FishSprite
from PondData import PondData
from Storage import Storage
from Log import get_logger

ASSET_DIR = path.join(path.dirname(__file__), "assets")


class Pond:
    UPDATE_DATA_EVENT = pygame.USEREVENT + 1
    PHEROMONE_EVENT = pygame.USEREVENT + 2

    def __init__(self, name: str = "doo-pond", storage: Storage = None):
        self.__name: str = name
        self.__data: PondData = PondData(name)
        self.__storage: Storage = storage
        self.__fish_school = FishSchool()
        self.__logger = get_logger("pond")

        self.__birth_rate = 0.01

    def get_name(self):
        return self.__name

    def __load_fishes(self):
        fishes = self.__storage.get_fishes()
        for fish in fishes:
            self.__fish_school.add_fish(fish)
        self.__logger.info(f"Loaded {len(fishes)} fishes")

    def spawn_fish(self, genesis: str = None, parent_id: str = None):
        genesis = genesis if genesis else self.__name
        sprite = fishFactory.generate_fish_sprite(genesis, parent_id)
        self.__fish_school.add_fish(sprite)
        self.__data.add_fish(sprite.get_data())
        if self.__storage:
            self.__storage.add_fish(sprite)
        self.__logger.info(f"Spawned fish {sprite.get_id()}")

    def remove_fish(self, fish: FishSprite):
        self.__fish_school.remove_fish(fish)

    def __update_fish(self, fish: FishSprite):
        if not fish.is_alive():
            # self.__fish_school.remove_fish(fish)
            # self.__data.remove_fish(fish.get_id())
            return
        fish.update_data()

        pheromone_value = random.randint(25, 50) * self.__birth_rate
        fish.add_pheromone(pheromone_value)

        if fish.is_pregnant():
            self.spawn_fish(fish.get_genesis(), fish.get_id())

        if fish.get_time_in_pond() >= 15:
            # Todo: migrate fish
            ...

    def run(self):
        pygame.init()
        pygame.display.set_caption(f"385dc-FishHaven [{self.__name}]")
        screen = pygame.display.set_mode(config.WINDOW_SIZE)
        background = pygame.image.load(path.join(ASSET_DIR, "background.jpg"))
        background = background.convert()
        background = pygame.transform.scale(background, config.WINDOW_SIZE)
        clock = pygame.time.Clock()

        pygame.time.set_timer(Pond.UPDATE_DATA_EVENT, 1000)
        pygame.time.set_timer(Pond.PHEROMONE_EVENT, 15000)

        if self.__storage:
            self.__load_fishes()

        self.spawn_fish()

        running = 1
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0

                if event.type == Pond.UPDATE_DATA_EVENT:
                    self.__fish_school.update_data(self.__update_fish)

                if event.type == Pond.PHEROMONE_EVENT:
                    # Todo: update pheromone
                    pass

            self.__fish_school.update_sprite()
            screen.blit(background, (0, 0))
            self.__fish_school.draw(screen)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    pond = Pond("doo-pond")
    pond.run()
