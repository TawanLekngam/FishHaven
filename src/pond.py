import random
import pygame
import sys
import threading

from PySide6.QtWidgets import QApplication

from data.pondData import PondData
from components import dashboard
from fish import Fish


class Pond:
    __WINDOW_SIZE = (1280, 720)

    def __init__(self):
        self.name: str = "doo-pond"
        self.all_sprites: pygame.sprite.Group[Fish] = pygame.sprite.Group()

    def spawn_fish(self, genesis):
        fish = Fish(genesis)
        self.all_sprites.add(fish)

    def __tick_lifetime(self):
        for fish in self.all_sprites:
            fish.tick_lifetime()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(Pond.__WINDOW_SIZE)
        bg = pygame.image.load("./src/assets/background.jpg")
        bg = pygame.transform.scale(bg, Pond.__WINDOW_SIZE)
        pygame.display.set_caption("Fish Haven [Doo Pond]")
        clock = pygame.time.Clock()

        update_time = pygame.time.get_ticks()

        self.spawn_fish("doo-pond")

        app = QApplication(sys.argv)

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # handle press key event
                if event.type == pygame.KEYDOWN:
                    print("press button")
                    if event.key == pygame.K_LEFT:
                        print("open dashboard")
                        d = dashboard.DashBoard()
                        pond_handler = threading.Thread(target=app.exec_)
                        pond_handler.start()
                    

            time_since_update = pygame.time.get_ticks() - update_time
            if (time_since_update >= 1000):
                self.__tick_lifetime()
                update_time = pygame.time.get_ticks()

            self.all_sprites.update()  # update all sprites in the group
            screen.blit(bg, (0, 0))  # render background image
            self.all_sprites.draw(screen)  # draw all sprites in the group

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    p = Pond()
    p.run()
