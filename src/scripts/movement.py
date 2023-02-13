from abc import ABC, abstractmethod
from pygame import sprite


class Movement(ABC):
    def __init__(self, speed: int):
        self.speed = speed

    @abstractmethod
    def move(self, target: sprite.Sprite):
        pass


class BounceMovement(Movement):
    def move(self, sprite):
        if sprite.direction == "left":
            sprite.rect.x -= self.speed
            if sprite.rect.x <= 0:
                sprite.direction = "right"
        else:
            sprite.rect.x += self.speed
            if sprite.rect.x >= 1280 - sprite.rect.width:
                sprite.direction = "left"


class VerticalMovement(Movement):
    def __init__(self, speed):
        self.speed = speed

    def move(self, sprite):
        sprite.rect.y += self.speed
        if sprite.rect.y >= 720 - sprite.rect.height:
            sprite.rect.y = 0