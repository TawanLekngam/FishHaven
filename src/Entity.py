import random
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List

from pygame import Rect, Surface
from pygame.sprite import Sprite


class Direction(str, Enum):
    LEFT = 'left'
    RIGHT = 'right'


class Entity(ABC, Sprite):
    area: Rect
    image: Surface
    rect: Rect
    direction: Dict[Direction, List[Surface]]

    def __init__(self):
        Sprite.__init__(self)

    def _random_position(self):
        self.rect.x = random.randrange(self.area.width - self.rect.width)
        self.rect.y = random.randrange(self.area.height - self.rect.height)

    @abstractmethod
    def update(self):
        pass
