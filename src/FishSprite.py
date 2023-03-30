import os.path as path
import random
from enum import Enum
import config

import pygame

from Entity import Direction, Entity
from FishData import FishData
from movements import Movement

ASSET_DIR = path.join(path.dirname(__file__), "assets")


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

        self.frame = 0
        self.direction = random.choice([Direction.LEFT, Direction.RIGHT])
        self.sprites = {
            Direction.LEFT: [],
            Direction.RIGHT: []
        }


        self._init_sprites()
        
        self.time_in_pond = 0
        self.size = Size.SMALL
        self.movement = movement

    def get_id(self):
        return self.__data.get_id()

    def get_genesis(self):
        return self.__data.get_genesis()

    def _init_sprites(self):
        pond_type = "local-pond" if self.get_genesis() == config.POND_NAME else "foreign-pond"
        for i in range(1, 5):
            image_path = path.join(ASSET_DIR, pond_type, f"{i}.png")
            surface = pygame.image.load(image_path)
            surface = pygame.transform.scale(surface, (100, 100))
            self.sprites[Direction.LEFT].append(surface)
            self.sprites[Direction.RIGHT].append(pygame.transform.flip(surface, True, False))
        self.image = self.sprites[self.direction][self.frame]
        self.rect = self.image.get_rect()
        self.area = pygame.display.get_surface().get_rect()
        self._random_position()

    def get_parent_id(self):
        return self.__data.get_parent_id()

    def get_state(self):
        return self.__data.get_state()

    def is_pregnant(self):
        if self.__data.get_pheromone() >= self.__data.get_pheromone_threshold():
            self.reset_pheromone()
            return True
        return False

    def is_immortal(self):
        return self.__data.get_lifespan() == 0

    def is_alive(self):
        return self.is_immortal() or self.__data.get_lifespan() > self.__data.get_age()

    def add_pheromone(self, amount: float):
        self.__data.set_pheromone(self.__data.get_pheromone() + amount)

    def reset_pheromone(self):
        self.__data.set_pheromone(0)

    def die(self):
        self.get_state("dead")
        self.kill()

    def get_data(self):
        return self.__data

    def update(self):
        self.__update_sprite()
        self.movement.move(self)

    def __update_sprite(self):
        self.frame = (self.frame + 0.1) % len(self.sprites[self.direction])
        self.image = self.sprites[self.direction][int(self.frame)]

    def __update_time(self):
        self.time_in_pond += 1
        if self.is_immortal():
            return

        self.__data.set_age(self.__data.get_age() + 1)
