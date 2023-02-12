import pygame
import sys
import threading

from PySide6.QtWidgets import QApplication

from components.Dashboard import DashBoard
from FishSprite import FishSprite
from utils.FishFactory import FishFactory


class Pond:
    __WINDOW_SIZE = (1280, 720)

    def __init__(self):
        self.name: str = "doo-pond"
        self.all_sprites: pygame.sprite.Group[FishSprite] = pygame.sprite.Group(
        )

    def spawn_fish(self):
        fish = FishFactory.generate_fish()
        fish_sprite = FishSprite(fish)
        self.all_sprites.add(fish_sprite)

    def __tick_lifespan(self):
        for fish in self.all_sprites:
            fish.tick_lifespan()

    def load_fishes(self):
        # TODO: Replace with database fetches
        for _ in range(5):
            self.spawn_fish()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(Pond.__WINDOW_SIZE)
        background = pygame.image.load("./src/assets/background.jpg").convert()
        background = pygame.transform.scale(background, Pond.__WINDOW_SIZE)
        pygame.display.set_caption("Fish Haven [Doo Pond]")
        clock = pygame.time.Clock()
        update_time = pygame.time.get_ticks()

        self.load_fishes()

        app = QApplication(sys.argv)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    print("press button")
                    if event.key == pygame.K_d:
                        print("open dashboard")
                        _ = DashBoard()
                        pond_handler = threading.Thread(target=app.exec_)
                        pond_handler.start()

            time_since_update = pygame.time.get_ticks() - update_time
            if time_since_update >= 1000:
                self.__tick_lifespan()
                update_time = pygame.time.get_ticks()

            self.all_sprites.update()  # update all sprites in the group
            screen.blit(background, (0, 0))  # render background image
            self.all_sprites.draw(screen)  # draw all sprites in the group

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
