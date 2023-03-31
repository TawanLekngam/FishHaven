import math
import random

from FishData import FishData
from FishSprite import FishSprite
from movements import BounceMovement


class FishFactory:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def generate_fish_data(self, genesis: str, parent_id: str = None) -> FishData:
        id = self.__rand_id()
        pheromone_threshold = self.__rand_pheromone_threshold()
        crowd_threshold = self.__rand_crowd_threshold()
        lifespan = self.__rand_lifespan()

        fish = FishData(id, genesis, pheromone_threshold,
                        crowd_threshold, lifespan, parent_id)
        return fish

    def generate_fish_sprite(self, genesis: str, parent_id: str = None) -> FishSprite:
        movement = self.__rand_movement()
        fish_sprite = FishSprite(
            self.generate_fish_data(genesis, parent_id), movement)
        return fish_sprite
    
    def generate_fish_by_data(self, fish_data: FishData) -> FishSprite:
        movement = self.__rand_movement()
        fish_sprite = FishSprite(fish_data, movement)
        return fish_sprite

    def __rand_id(self) -> str:
        id = ""
        for _ in range(6):
            id += "0123456789"[math.floor(random.random() * 10)]
        return id

    def __rand_pheromone_threshold(self):
        return random.randint(30, 60)

    def __rand_crowd_threshold(self):
        return random.randint(5, 20)

    def __rand_lifespan(self):
        return 0 if random.random() <= 0.001 else random.randint(5, 10)

    def __rand_movement(self):
        speed = random.randint(1, 5)
        movement = random.choice([BounceMovement])
        return movement(speed)


fishFactory = FishFactory()
