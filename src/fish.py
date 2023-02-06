import os
import random
import pygame

from data.fishData import FishData


BASE_DIR = os.path.split(os.path.abspath(__file__))[0]
ASSET_DIR = os.path.join(BASE_DIR, "assets")


class Fish(pygame.sprite.Sprite):
    def __init__(self, genesis: str, data: FishData = None):
        super().__init__()
        self.data = data if data else FishData(genesis)

        # pygame objects
        self.direction = random.choice(["left", "right"])
        self.frame = 0
        self.sprites: dict[str, list[pygame.Surface]] = {
            "left": [],
            "right": []
        }
        self.__load_sprite(genesis)
        self.image = self.sprites[self.direction][self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1280 - self.rect.width)
        self.rect.y = random.randint(0, 720 - self.rect.height)
        self.speed = random.randint(1, 3)

    def __load_sprite(self, genesis: str):
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

    def __move(self):
        if self.direction == "left":
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.direction = "right"
        else:
            self.rect.x += self.speed
            if self.rect.x >= 1280 - self.rect.width:
                self.direction = "left"

    def tick_lifetime(self):
        if self.data.is_immortal:
            return

        if self.data.is_alive:
            self.data.lifetime -= 1
            self.data.time_in_pond += 1
            if self.data.lifetime <= 0:
                self.data.is_alive = False
                self.kill()
        print(f"id:{self.data.id} lefetime:{self.data.lifetime}")

    def update(self):
        self.frame = (self.frame + 0.1) % len(self.sprites[self.direction])
        self.image = self.sprites[self.direction][int(self.frame)]
        self.__move()

    def die(self):
        self.kill()
