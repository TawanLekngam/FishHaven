import pygame
from pygame.sprite import Group
from random import randint

from storage import Storage
from fish import Fish
from model import FishModel


FPS = 30
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class Pond:
    def __init__(self, name):
        self.name = name
        self.storage: Storage = None

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.name)
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        clock = pygame.time.Clock()

        allSprites = Group()

        # self._spawnFish(allSprites)  # debug: spawn a fish
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self._spawnFish(allSprites)

            allSprites.update()
            screen.fill((0, 0, 0))
            allSprites.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)

    def stop(self):
        pass

    def _spawnFish(self, group: Group, genesis: str = None):
        def generateId():
            id = ""
            for _ in range(6):
                id += str(randint(0, 9))
            return id

        if genesis is None:
            genesis = self.name

        model = FishModel(generateId(), genesis)
        fish = Fish(model)
        group.add(fish)


if __name__ == "__main__":
    pond = Pond("dooPond")
    pond.start()
