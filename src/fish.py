from __future__ import annotations

from os import listdir
from os.path import join, isdir
from pygame.image import load
from pygame.rect import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.display import get_surface
from pygame.transform import flip, scale
from typing import List, Dict, AnyStr
from enum import Enum

from model import FishModel
from setting import PATH

SCALE = (100, 100)


class Direction(Enum):
    LEFT = 0
    RIGHT = 1


class Fish(Sprite):
    skinL: Dict[AnyStr, List[Surface]] = {}
    skinR: Dict[AnyStr, List[Surface]] = {}

    def __init__(self, model: FishModel):
        super().__init__()
        self.model = model
        self._loadSkin(model.genesis)
        self.image: Surface = Fish.skinL[model.genesis][0]
        self.frame = 0
        self.direction: Direction = Direction.RIGHT
        self.rect: Rect = self.image.get_rect()

    def _loadSkin(self, genesis: str):
        if genesis not in Fish.skinL:
            path = join(PATH["assets"], genesis)

            if isdir(path):
                files = [f for f in listdir(path) if f.endswith(".png")]
                print("f", files)
                print("g", genesis)
                Fish.skinL[genesis] = [
                    scale(load(join(path, f)), SCALE) for f in files]
                Fish.skinR[genesis] = [flip(s, True, False)
                                       for s in Fish.skinL[genesis]]

    def update(self):
        # self.movement.move(self)
        self.move()

    def updateImage(self):
        if self.direction == Direction.LEFT:
            self.image = Fish.skinL[self.model.genesis][int(self.frame)]
        else:
            self.image = Fish.skinR[self.model.genesis][int(self.frame)]

    def move(self):
        screenRect = get_surface().get_rect()
        if self.direction == Direction.LEFT:
            self.rect.x -= 1
            if self.rect.left < screenRect.left:
                self.direction = Direction.RIGHT

        else:
            self.rect.x += 1
            if self.rect.right > screenRect.right:
                self.direction = Direction.LEFT
        self.frame = (self.frame + 0.1) % len(Fish.skinL[self.model.genesis])
        self.updateImage()
