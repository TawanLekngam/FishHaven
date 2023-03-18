import os
import random
import pygame

from models import Fish
from scripts import Movement, BounceMovement, VerticalMovement


BASE_DIR = os.path.split(os.path.abspath(__file__))[0]
ASSET_DIR = os.path.join(BASE_DIR, "assets")


class FishSprite(pygame.sprite.Sprite):
    def __init__(self, fish: Fish, movement: Movement = BounceMovement(3)):
        super().__init__()
        self.fish = fish

        # pygame objects
        self.direction = random.choice(["left", "right"])
        self.frame = 0
        self.sprites: dict[str, list[pygame.Surface]] = {
            "left": [],
            "right": []
        }
        self.__load_sprite(fish.get_genesis())
        self.image = self.sprites[self.direction][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1280 - self.rect.width)
        self.rect.y = random.randint(0, 720 - self.rect.height)

        self.movement = movement

    def __load_sprite(self, genesis: str):
        pond_type = "local_pond" if genesis == "doo-pond" else "foreign_pond"
        target_path = os.path.join(ASSET_DIR, pond_type)

        for i in range(1, 5):
            image_path = f"{target_path}/{i}.png"
            image = pygame.image.load(image_path).convert_alpha()
            image_left = pygame.transform.scale(image, (100, 100))
            image_right = pygame.transform.flip(image_left, True, False)
            self.sprites["left"].append(image_left)
            self.sprites["right"].append(image_right)

        self.frame = 0

    def tick_lifespan(self):
        if self.fish.is_immortal:
            return

        if self.fish.is_alive:
            self.fish.lifespan -= 1
            self.fish.time_in_pond += 1
            if self.fish.lifespan <= 0:
                self.fish.is_alive = False
                self.kill()
        # print(f"id:{self.fish.id} lifespan:{self.fish.lifespan}")

    def get_data(self):
        return self.fish

    def update(self):
        self.movement.move(self)
        self.frame = (self.frame + 0.1) % len(self.sprites[self.direction])
        self.image = self.sprites[self.direction][int(self.frame)]

    def die(self):
        self.kill()
