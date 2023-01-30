import random
import pygame


class Fish(pygame.sprite.Sprite):
    def __init__(self, genesis: str):
        super().__init__()

        self.direction = random.choice(["left", "right"])
        self.current_frame = 0
        self.sprites: dict[str, list[pygame.Surface]] = {
            "left": [],
            "right": []
        }

        self.__load_sprite(genesis)
        self.image = self.sprites[self.direction][self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1280 - self.rect.width)
        self.rect.y = random.randint(0, 720 - self.rect.height)

    def __load_sprite(self, genesis: str):
        pond_type = "local_pond" if genesis == "doo-pond" else "foreign_pond"
        base_path = f"./src/assets/{pond_type}"

        for i in range(1, 5):
            image_path = f"{base_path}/{i}.png"
            image = pygame.image.load(image_path)
            image_left = pygame.transform.scale(image, (100, 100))
            image_right = pygame.transform.flip(image_left, True, False)
            self.sprites["left"].append(image_left)
            self.sprites["right"].append(image_right)

        self.current_frame = 0

    def move(self):
        if self.direction == "left":
            self.rect.x -= random.randint(1, 3)
            if self.rect.x <= 0:
                self.direction = "right"
        else:
            self.rect.x += random.randint(1, 3)
            if self.rect.x >= 1280 - self.rect.width:
                self.direction = "left"

    def update(self):
        self.current_frame = (self.current_frame + 0.1) % len(self.sprites[self.direction])
        self.image = self.sprites[self.direction][int(self.current_frame)]
        self.move()

    def die(self):
        self.kill()
