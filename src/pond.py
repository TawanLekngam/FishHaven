import random
import pygame

from data.pondData import PondData
from fish import Fish


class Pond:
    __WINDOW_SIZE = (1280, 720)

    def __init__(self):
        self.name: str = "doo-pond"
        self.all_sprites = pygame.sprite.Group()

    def spawn_fish(self, genesis):
        fish = Fish(genesis)
        self.all_sprites.add(fish)

    def migrate(self):
        pass

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(Pond.__WINDOW_SIZE)
        bg = pygame.image.load("./src/assets/background.jpg")
        bg = pygame.transform.scale(bg, Pond.__WINDOW_SIZE)
        pygame.display.set_caption("Fish Haven [Doo Pond]")
        clock = pygame.time.Clock()

        self.spawn_fish("doo-pond")
        self.spawn_fish("other")

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.all_sprites.update()  # update all sprites in the group
            screen.blit(bg, (0, 0))  # render background image
            self.all_sprites.draw(screen)  # draw all sprites in the group

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    p = Pond()
    p.run()
