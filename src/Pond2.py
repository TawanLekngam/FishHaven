import pygame
import os.path as path
from PondData import PondData
from FishSchool import FishSchool

from factories import fishFactory
import config

ASSET_DIR = path.join(path.dirname(__file__), "assets")

class Pond:
    UPDATE_DATA_EVENT = pygame.USEREVENT + 1

    def __init__(self, name: str = "doo-pond"):
        self.__name: str = name
        self.data: PondData = PondData(name)
        self.fish_school = FishSchool()

    def get_name(self):
        return self.__name

    def spawn_fish(self, genesis: str = None, parent_id: str = None):
        genesis = genesis if genesis else self.__name
        sprite = fishFactory.generate_fish_sprite(genesis, parent_id)
        self.data.add_fish(sprite.get_data())
        self.fish_school.add_fish(sprite)

    def run(self):
        pygame.init()
        pygame.display.set_caption(f"385dc-FishHaven [{self.__name}]")
        screen = pygame.display.set_mode(config.WINDOW_SIZE)
        background = pygame.image.load(path.join(ASSET_DIR,"background.jpg")).convert()
        background = pygame.transform.scale(background, config.WINDOW_SIZE)
        clock = pygame.time.Clock()

        pygame.time.set_timer(Pond.UPDATE_DATA_EVENT, 1000)

        self.spawn_fish()

        running = 1
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = 0

                if event.type == Pond.UPDATE_DATA_EVENT:...

            self.fish_school.update()
            screen.blit(background, (0, 0))
            self.fish_school.draw(screen)
            pygame.display.flip()


if __name__ == "__main__":
    pond = Pond("doo-pond")
    pond.run()
