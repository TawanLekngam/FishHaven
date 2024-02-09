from __future__ import annotations

from enum import Enum
from typing import List, Dict, AnyStr
from random import randint
from time import time

from os import listdir
from os.path import join, isdir

from pygame.display import get_surface
from pygame.image import load
from pygame.rect import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.transform import flip, scale

from model import FishModel
from setting import PATH


SCALE = (100, 100)


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


class Fish(Sprite):
    skin_l: Dict[AnyStr, List[Surface]] = {}
    skin_r: Dict[AnyStr, List[Surface]] = {}

    direction_x: Direction
    direction_y: Direction
    image: Surface
    rect: Rect
    speed: int = 3

    def __init__(self, model: FishModel):
        super().__init__()
        self.model = model
        self.frame = 0

        self._current_time = time()

        self._load_skin(model.genesis)
        self._random_position()
        self._random_direction()

    def _load_skin(self, genesis: str):
        if genesis not in Fish.skin_l:
            path = join(PATH["assets"], genesis)

            if isdir(path):
                files = [f for f in listdir(path) if f.endswith(".png")]
                Fish.skin_l[genesis] = [scale(load(join(path, f)), SCALE)
                                        for f in files]
                Fish.skin_r[genesis] = [flip(s, True, False)
                                        for s in Fish.skin_l[genesis]]

        self.image = Fish.skin_l[genesis][0]
        self.rect = self.image.get_rect()

    def update(self):
        self._update_time()
        self._move()

    def _update_image(self):
        self.frame = (self.frame + 0.1) % len(Fish.skin_l[self.model.genesis])
        if self.direction_x == Direction.LEFT:
            self.image = Fish.skin_l[self.model.genesis][int(self.frame)]
        else:
            self.image = Fish.skin_r[self.model.genesis][int(self.frame)]

    def _move(self):
        screen_rect = get_surface().get_rect()
        if self.direction_x == Direction.LEFT:
            self.rect.x -= self.speed
            if self.rect.left < screen_rect.left:
                self.direction_x = Direction.RIGHT
        else:
            self.rect.x += self.speed
            if self.rect.right > screen_rect.right:
                self.direction_x = Direction.LEFT

        if self.direction_y == Direction.UP:
            self.rect.y -= self.speed
            if self.rect.top < screen_rect.top:
                self.direction_y = Direction.DOWN
        else:
            self.rect.y += self.speed
            if self.rect.bottom > screen_rect.bottom:
                self.direction_y = Direction.UP
        self._update_image()

    def _random_position(self):
        screen_rect = get_surface().get_rect()
        self.rect.x = randint(0, screen_rect.width - self.rect.width)
        self.rect.y = randint(0, screen_rect.height - self.rect.height)

    def _random_direction(self):
        self.direction_x = Direction(randint(0, 1))
        self.direction_y = Direction(randint(2, 3))

    def _update_time(self):
        if not self.is_alive():
            self.kill()
            return

        if time() - self._current_time > 1:
            self._current_time = time()
            self.model.lifespan -= 1

    def is_alive(self):
        return self.model.lifespan > 0
