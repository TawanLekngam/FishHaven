from __future__ import annotations
import os
import random
from typing import Callable
import pygame

from .FishData import FishData


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_DIR = os.path.join(BASE_DIR, "assets")


class FishSprite(pygame.sprite.Sprite):
    sprites: dict[str, list[pygame.Surface]] = {
        "left": [],
        "right": []
    }

    def __init__(self, data: FishData, movement: Callable[[FishSprite], None]):
        super().__init__()
        self.data = data

        self.direction = random.choice(["left", "right"])
        self.frame = 0

        self._load_sprite(data.get_genesis())
        self.image = self.sprites[self.direction][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1280 - self.rect.width)
        self.rect.y = random.randint(0, 720 - self.rect.height)

        self.movement = movement

        # TODO: Feed fish system
        self.health = 100
        self.hunger = 100

    def _load_sprite(self, genesis: str):
        pond_type = "local_pond" if genesis == "doo-pond" else "foreign_pond"
        target_path = os.path.join(ASSET_DIR, pond_type)

        for i in range(1, 5):
            image_path = f"{target_path}/{i}.png"
            image = pygame.image.load(image_path)
            image_left = pygame.transform.scale(image, (100, 100))
            image_right = pygame.transform.flip(image_left, True, False)
            self.sprites["left"].append(image_left)
            self.sprites["right"].append(image_right)

        self.frame = 0

    def tick_life_span(self):
        if self.data.is_immortal:
            return

        if not self.data.is_alive:
            self.die()
        self.data.life_span -= 1
        self.data.time_in_pond += 1

    def get_data(self):
        return self.data

    def get_id(self):
        return self.data.get_id()

    def get_genesis(self):
        return self.data.get_genesis()

    def get_in_pond_time(self):
        return self.data.time_in_pond

    def update(self):
        """Update fish sprite"""
        self.frame = (self.frame + 0.1) % len(self.sprites[self.direction])
        self.image = self.sprites[self.direction][int(self.frame)]
        self.movement.move(self)

    def update_data(self):
        """Update fish data"""
        self.tick_life_span()

    def is_alive(self):
        return self.data.is_alive()

    def is_pregnant(self):
        """Check if fish is pregnant"""
        if self.get_pheromone() < self.get_pheromone_threshold():
            return False
        self.reset_pheromone()
        return True

    def get_crowd_threshold(self):
        return self.data.get_crowd_threshold()

    def get_pheromone(self):
        return self.data.get_pheromone()

    def add_pheromone(self, amount: int):
        self.data.pheromone += amount

    def get_pheromone_threshold(self):
        return self.data.get_pheromone_threshold()

    def reset_pheromone(self):
        self.data.pheromone = 0

    def die(self):
        self.kill()


if __name__ == "__main__":
    print(ASSET_DIR)
