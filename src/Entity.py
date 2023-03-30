from abc import ABC, abstractmethod
from pygame import Surface, Rect, display
from pygame.sprite import Sprite
from typing import List, Dict
from enum import Enum


class Direction(str, Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


class Entity(ABC, Sprite):
    area: Rect = display.get_surface().get_rect()
    image: Surface
    rect: Rect
    direction: Dict[Direction, List[Surface]]

    def __init__(self):
        Sprite.__init__()

    @abstractmethod
    def update(self):
        pass
