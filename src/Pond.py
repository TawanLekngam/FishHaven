import random
import sys

import pygame
from PySide6.QtWidgets import QApplication

from components import MainDashboard
from factories import fishFactory
from FishSchool import FishSchool
from FishSprite import FishSprite
from PondData import PondData
from Storage import Storage


class Pond:
    WINDOW_SIZE = (1280, 720)
    UPDATE_EVENT = pygame.USEREVENT + 1
    PHEROMONE_EVENT = pygame.USEREVENT + 2
    BIRTH_RATE = 0.05

    def __init__(self, name: str, storage: Storage):
        self.name: str = name
        self.data: PondData = PondData(name)
        self.storage: Storage = storage
        self.fish_school = FishSchool()
        self.__load_fishes()

    def __load_fishes(self):
        for fish in self.storage.get_fishes().values():
            self.fish_school.add_fish(fish)

    def spawn_fish(self, genesis: str = None, parent_id: str = None):
        genesis = genesis if genesis else self.name
        sprite = fishFactory.generate_fish_sprite(genesis, parent_id)
        self.storage.add_fish(sprite.get_data())
        self.fish_school.add_fish(sprite)

    def remove_fish(self, fish: FishSprite):
        self.fish_school.remove(fish)

    def get_fishes(self):
        fishes = []
        for fish in self.fish_school:
            fishes.append(fish.get_data())
        return fishes

    def get_population(self):
        return self.fish_school.get_population()

    def update(self):
        self.fish_school.update_fishes(self.__update_fish)
        self.__update_dashboard()

    def __update_fish(self, fish: FishSprite):
        fish.update_data()
        if not fish.is_alive():
            self.fish_school.remove(fish)
            self.storage.remove_fish(fish.get_id())
            return

        pheromone_value = random.randint(25, 50) * Pond.BIRTH_RATE
        fish.add_pheromone(pheromone_value)

        if fish.is_pregnant():
            self.spawn_fish(fish.get_genesis(), fish.get_id())

        if fish.get_in_pond_time() >= 15:
            self.remove_fish(fish)

        if self.get_population() > fish.get_crowd_threshold():
            self.remove_fish(fish)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(Pond.WINDOW_SIZE)
        background = pygame.image.load("./src/assets/background.jpg").convert()
        background = pygame.transform.scale(background, Pond.WINDOW_SIZE)
        pygame.display.set_caption("Fish Haven [Doo Pond]")
        clock = pygame.time.Clock()

        app = QApplication(sys.argv)
        dashboard = MainDashboard()

        pygame.time.set_timer(Pond.UPDATE_EVENT, 1000)
        pygame.time.set_timer(Pond.PHEROMONE_EVENT, 15000)

        running = 1
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        dashboard.show()

                if event.type == Pond.UPDATE_EVENT:
                    dashboard.update(dp_data=self.get_population())
                    self.update()

            self.fish_school.update()
            screen.blit(background, (0, 0))
            self.fish_school.draw(screen)

            pygame.display.flip()
            clock.tick(60)
            app.processEvents()

        pygame.quit()
