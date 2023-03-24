import pygame
import sys
import random
import logging

from PySide6.QtWidgets import QApplication


from Storage import Storage
from components import MainDashboard
from models import FishSprite, FishSchool, PondData

from scripts.movement import BounceMovement
from utils import fish_factory


class Pond:
    __WINDOW_SIZE = (1280, 720)

    __UPDATE_EVENT = pygame.USEREVENT + 1
    __PHEROMONE_EVENT = pygame.USEREVENT + 2

    __BIRTH_RATE = 0.005

    def __init__(self, name: str, storage: Storage):
        self.name: str = name
        self.data: PondData = PondData(name)
        self.storage: Storage = storage
        self.fish_school = FishSchool()

        pond_log = logging.getLogger("pond")
        pond_log.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        pond_log.addHandler(ch)
        self.log = pond_log

        self.app = QApplication(sys.argv)
        self.dashboard = MainDashboard(self, self.fish_school)
        self.dashboard.show()
        self.__load_fishes()

    def __load_fishes(self):
        """Load fishes from the redis storage"""
        for fish in self.storage.get_fishes().values():
            self.fish_school.add_fish(fish)

        self.log.info(
            f"loaded {len(self.fish_school)} fishes from the Redis storage")

    def spawn_fish(self, genesis: str = None, parent_id: str = None):
        """Spawn a new fish in the pond"""
        genesis = genesis if genesis else self.name
        fish = fish_factory.generate_fish(genesis, parent_id)
        fish_sprite = FishSprite(fish, BounceMovement(3))
        self.storage.add_fish(fish)
        self.fish_school.add_fish(fish_sprite)
        self.log.info(f"spawned a new fish {fish.get_id()}")

    def remove_fish(self, fish: FishSprite):
        self.fish_school.remove(fish)

    def get_fishes(self):
        fishes = []
        for fish in self.fish_school:
            fishes.append(fish.get_data())
        return fishes

    def get_population(self):
        return self.fish_school.get_total()

    def update(self):
        self.fish_school.update_fishes(self.__update_fish)


    def __update_fish(self, fish: FishSprite):
        fish.update_data()
        if not fish.is_alive():
            self.fish_school.remove(fish)
            self.storage.remove_fish(fish.get_id())
            return

        pheromone_value = random.randint(25, 50) * Pond.__BIRTH_RATE
        fish.add_pheromone(pheromone_value)

        if fish.is_pregnant():
            self.spawn_fish(fish.get_genesis(), fish.get_id())

        if fish.get_in_pond_time() >= 15:
            self.remove_fish(fish)

        if self.get_population() > fish.get_crowd_threshold():
            self.remove_fish(fish)

    def run(self):
        """Run the pond simulation"""
        pygame.init()
        screen = pygame.display.set_mode(Pond.__WINDOW_SIZE)
        background = pygame.image.load("./src/assets/background.jpg").convert()
        background = pygame.transform.scale(background, Pond.__WINDOW_SIZE)
        pygame.display.set_caption("Fish Haven [Doo Pond]")
        clock = pygame.time.Clock()

        # for _ in range(5):
        #     self.spawn_fish()

        pygame.time.set_timer(Pond.__UPDATE_EVENT, 1000)
        pygame.time.set_timer(Pond.__PHEROMONE_EVENT, 15000)

        running = 1
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self.dashboard.show()

                if event.type == Pond.__UPDATE_EVENT:
                    self.dashboard.update()
                    self.update()
                
                if event.type == Pond.__PHEROMONE_EVENT:
                    self.log.info("Pheromone event triggered")

            self.fish_school.update()
            screen.blit(background, (0, 0))
            self.fish_school.draw(screen)

            pygame.display.flip()
            clock.tick(60)
            self.app.processEvents()

        pygame.quit()
