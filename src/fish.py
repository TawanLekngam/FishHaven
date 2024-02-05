from __future__ import annotations

from os import listdir
from os.path import join, isdir
from pygame.image import load
from pygame.rect import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface
from pygame.transform import flip, scale
from typing import List, Dict, AnyStr

from model import FishModel
from setting import PATH

SCALE = (100, 100)


class Fish(Sprite):
    skinL: Dict[AnyStr, List[Surface]] = {}
    skinR: Dict[AnyStr, List[Surface]] = {}

    def __init__(self, model: FishModel, movement: Movement):
        super().__init__()
        self.model = model
        self.movement = movement
        self._loadSkin(model.genesis)
        self.image: Surface = Fish.skinL[model.genesis][0]
        self.rect: Rect = self.image.get_rect()

    def _loadSkin(self, genesis: str):
        if genesis not in Fish.skinL:
            path = join(PATH["assets"], genesis)

            if isdir(path):
                files = [f for f in listdir(path) if f.endswith(".png")]
                print("f", files)
                print("g", genesis)
                Fish.skinL[genesis] = [scale(load(join(path, f)), SCALE) for f in files]
                Fish.skinR[genesis] = [flip(s, True, False) for s in Fish.skinL[genesis]]

    def update(self):
        # self.movement.move(self)
        pass


class Movement:
    def __init__(self, speed):
        self.speed = speed

    def move(self, f: Fish, screenRect: Rect):
        pass
