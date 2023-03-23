import pygame
import sys
import random

from PySide6.QtWidgets import QApplication

from utils.FishFactory import FishFactory

from Storage import Storage
from components import MainDashboard
from models import FishSprite, FishGroup, PondData


fish_factory = FishFactory()


class Pond:
    __WINDOW_SIZE = (1280, 720)

    __UPDATE_EVENT = pygame.USEREVENT + 1
    __PHEROMONE_EVENT = pygame.USEREVENT + 2

    __BIRTH_RATE = 0.1

    def __init__(self, name: str, storage: Storage = None):
        self.name: str = name
        self.data: PondData = PondData(name)
        self.storage: Storage = storage
        self.fish_group = FishGroup()

        if self.storage:
            self.load_fishes()

    def spawn_fish(self, genesis: str = None, parent_id: str = None):
        genesis = genesis if genesis else self.name
        fish = fish_factory.generate_fish(genesis, parent_id)
        fish_sprite = FishSprite(fish)
        self.storage.add_fish(fish)
        self.fish_group.add_fish(fish_sprite)

    def remove_fish(self, fish: FishSprite):
        self.fish_group.remove(fish)

    def load_fishes(self):
        for fish in self.storage.get_fishes().values():
            self.fish_group.add_fish(fish)

    def get_fishes(self):
        fishes = []
        for fish in self.fish_group:
            fishes.append(fish.get_data())
        return fishes

    def get_population(self):
        return self.fish_group.get_total()

    def update(self):
        self.fish_group.update_fishes(self.__update_fish)

    def __update_fish(self, fish: FishSprite):
        print("update event", fish.get_id())
        fish.update_data()
        if not fish.is_alive():
            self.fish_group.remove(fish)
            self.storage.remove_fish(fish.get_id())
            return

        pheromone_value = random.randint(25, 50) * Pond.__BIRTH_RATE
        print("pheromone_value: ", pheromone_value)
        fish.add_pheromone(pheromone_value)

        if fish.is_pregnant():
            self.spawn_fish(fish.get_genesis(), fish.get_id())

        if fish.get_in_pond_time() >= 15:
            self.remove_fish(fish)

        if self.get_population() > fish.get_crowd_threshold():
            self.remove_fish(fish)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(Pond.__WINDOW_SIZE)
        background = pygame.image.load("./src/assets/background.jpg").convert()
        background = pygame.transform.scale(background, Pond.__WINDOW_SIZE)
        pygame.display.set_caption("Fish Haven [Doo Pond]")
        clock = pygame.time.Clock()
        update_time = pygame.time.get_ticks()

        self.load_fishes()

        for _ in range(20):
            self.spawn_fish()

        app = QApplication(sys.argv)
        dashboard = MainDashboard()

        pygame.time.set_timer(Pond.__UPDATE_EVENT, 1000)
        pygame.time.set_timer(Pond.__PHEROMONE_EVENT, 15000)

        running = 1
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        dashboard.show()

                if event.type == Pond.__UPDATE_EVENT:
                    self.update()

            time_since_update = pygame.time.get_ticks() - update_time
            if time_since_update >= 1000:
                dashboard.update(dp_data=self.get_population())
                update_time = pygame.time.get_ticks()

            self.fish_group.update()
            screen.blit(background, (0, 0))
            self.fish_group.draw(screen)

            pygame.display.flip()
            clock.tick(60)
            app.processEvents()

        pygame.quit()
