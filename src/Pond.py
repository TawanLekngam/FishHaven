import pygame
import sys

from PySide6.QtWidgets import QApplication

from utils.FishFactory import FishFactory

from Storage import Storage
from components import MainDashboard
from models import FishSprite, FishGroup


fish_factory = FishFactory()


class Pond:
    __WINDOW_SIZE = (1280, 720)

    def __init__(self, name: str, storage: Storage):
        self.name: str = name
        self.storage: Storage = storage

        self.all_sprites = FishGroup()

    def spawn_fish(self, genesis: str = None):
        genesis = genesis if genesis else self.name
        fish = fish_factory.generate_fish(genesis)
        fish_sprite = FishSprite(fish)
        self.storage.add_fish(fish)
        self.all_sprites.add(fish_sprite)

    def __tick_lifespan(self):
        for fish in self.all_sprites:
            fish.tick_lifespan()

    def load_fishes(self):
        for fish in self.storage.get_fishes().values():
            self.all_sprites.add(fish)

    def get_fishes(self):
        fishes = []
        for fish in self.all_sprites:
            fishes.append(fish.get_data())
        return fishes

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(Pond.__WINDOW_SIZE)
        background = pygame.image.load("./src/assets/background.jpg").convert()
        background = pygame.transform.scale(background, Pond.__WINDOW_SIZE)
        pygame.display.set_caption("Fish Haven [Doo Pond]")
        clock = pygame.time.Clock()
        update_time = pygame.time.get_ticks()

        self.load_fishes()
        self.spawn_fish()

        app = QApplication(sys.argv)
        dashboard = MainDashboard()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        dashboard.show()

            time_since_update = pygame.time.get_ticks() - update_time
            if time_since_update >= 1000:
                self.__tick_lifespan()
                dashboard.update(dp_data=self.get_fishes())
                update_time = pygame.time.get_ticks()

            self.all_sprites.update()
            screen.blit(background, (0, 0))
            self.all_sprites.draw(screen)

            pygame.display.flip()
            clock.tick(60)
            app.processEvents()

        pygame.quit()
