import os.path as path
from typing import Dict, List

import pygame

import config
from Entity import Direction, Entity
from movements import BounceMovement


class ZombieFishSprite(Entity):
    __cache: Dict[Direction, List[pygame.Surface]] = {}

    def __new__(self):
        if not ZombieFishSprite.__cache:
            image_path = path.join(config.ASSET_DIR, "zombie-fish.png")
            surface = pygame.image.load(image_path)
            surface = surface.convert_alpha()
            surface = pygame.transform.scale(surface, (150, 150))
            ZombieFishSprite.__cache[Direction.LEFT] = [surface]
            ZombieFishSprite.__cache[Direction.RIGHT]= [pygame.transform.flip(surface, True, False)]
        return super().__new__(self)

    def __init__(self):
        Entity.__init__(self)
        self.direction = Direction.LEFT
        self.__init_sprite()
        self.movement = BounceMovement()

    def __init_sprite(self):
        self.image = ZombieFishSprite.__cache[self.direction][0]
        self.rect = self.image.get_rect()
        self.area = pygame.display.get_surface().get_rect()
        self._random_position()

    def update(self):
        self.movement.move(self)
        self.image = ZombieFishSprite.__cache[self.direction][0]
