import random
import pygame

from data.pondData import PondData


class Pond:
    __WINDOW_SIZE = (1280, 720)

    def __init__(self):
        self.name: str = "doo-pond"
        self.capacity: int = 1000
        self.fish_count = 0
        self.fishes = []
        self.spawn_rate = 0.05
        self.time_since_last_spawn = 0

        # data
        self.pond_data: PondData = PondData(self.name)
        self.network = None

        # pygame
        self.sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

    def spawn_fish(self) -> None:
        pass

    def shutdown(self):
        pass

    def migrate(self):
        pass

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(Pond.__WINDOW_SIZE)
        bg = pygame.image.load("./src/assets/backgound.jpg")
        bg = pygame.transform.scale(bg, Pond.__WINDOW_SIZE)
        pygame.display.set_caption("Fish Haven [Doo Pond]")
        clock = pygame.time.Clock()

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))
            screen.blit(bg, (0, 0))

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    p = Pond()
    p.run()
