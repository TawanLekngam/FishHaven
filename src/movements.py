from Entity import Entity, Direction
from abc import ABC, abstractmethod


class Movement(ABC):
    def __init__(self, speed: int = 3):
        self.speed = speed

    @abstractmethod
    def move(self, target: Entity): ...


class BounceMovement(Movement):
    def move(self, target: Entity):
        if target.direction == Direction.LEFT:
            target.rect.x -= self.speed
            if target.rect.x < 0:
                target.direction = Direction.RIGHT
        elif target.direction == Direction.RIGHT:
            target.rect.x += self.speed
            if target.rect.x > target.area.width - target.rect.width:
                target.direction = Direction.LEFT
