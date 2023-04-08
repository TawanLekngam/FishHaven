import os.path as path
import random
from enum import Enum

import pygame

import config
from Entity import Direction, Entity
from FishData import FishData
from movements import Movement


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class LifeState(str, Enum):
    ALIVE = "alive"
    DEAD = "dead"


class FishSprite(Entity):

    def __init__(self, data: FishData, movement: Movement):
        Entity.__init__(self)
        self.__data = data
        self.__status = "in-pond"

        self.__frame = 0
        self.direction = random.choice([Direction.LEFT, Direction.RIGHT])
        self.sprites = {
            Direction.LEFT: [],
            Direction.RIGHT: []
        }

        self._init_sprites()

        self.__time_in_pond = 0
        self.__size = Size.SMALL
        self.__movement = movement

    def get_id(self):
        return self.__data.get_id()

    def get_genesis(self):
        return self.__data.get_genesis()

    def _init_sprites(self):
        pond_type = "local-pond" if self.get_genesis() == config.POND_NAME else "foreign-pond"
        for i in range(1, 5):
            image_path = path.join(config.ASSET_DIR, pond_type, f"{i}.png")
            surface = pygame.image.load(image_path)
            surface = surface.convert_alpha()
            surface = pygame.transform.scale(surface, (100, 100))
            self.sprites[Direction.LEFT].append(surface)
            self.sprites[Direction.RIGHT].append(
                pygame.transform.flip(surface, True, False))
        self.image = self.sprites[self.direction][self.__frame]
        self.rect = self.image.get_rect()
        self.area = pygame.display.get_surface().get_rect()
        self._random_position()

    def get_parent_id(self) -> str:
        return self.__data.get_parent_id()

    def get_data(self) -> FishData:
        return self.__data

    def get_image(self) -> pygame.Surface:
        return self.image

    def get_status(self) -> str:
        return self.__status

    def get_time_in_pond(self) -> int:
        return self.__time_in_pond

    def get_age(self) -> int:
        return self.__data.get_age()
    
    def get_pheromone(self) -> int:
        return int(self.__data.get_pheromone())
    
    def get_pheromone_threshold(self) -> int:
        return self.__data.get_pheromone_threshold()

    def get_lifespan(self) -> int:
        return self.__data.get_lifespan()

    def is_pregnant(self):
        if self.__data.get_pheromone() >= self.__data.get_pheromone_threshold():
            self.reset_pheromone()
            return True
        return False

    def is_immortal(self):
        return self.__data.get_lifespan() == 0

    def is_alive(self):
        return self.is_immortal() or self.get_age() < self.get_lifespan()

    def add_pheromone(self, amount: float):
        self.__data.set_pheromone(self.__data.get_pheromone() + amount)

    def reset_pheromone(self):
        self.__data.set_pheromone(0)

    def die(self):
        self.kill()

    def update(self):
        self.update_sprite()

    def update_sprite(self):
        self.__frame = (self.__frame + 0.1) % len(self.sprites[self.direction])
        self.image = self.sprites[self.direction][int(self.__frame)]
        self.__movement.move(self)

    def update_data(self):
        self.__time_in_pond += 1
        self.__data.set_age(self.__data.get_age() + 1)
        if not self.is_alive():
            self.__status = "dead"
            self.die()
