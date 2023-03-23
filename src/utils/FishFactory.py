import math
import random
from models import FishData


class FishFactory:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def generate_fish(self, genesis: str, parent_id:str=None) -> FishData:
        id = self.__rand_id()
        pheromone_threshold = self.__rand_pheromone_threshold()
        crowd_threshold = self.__rand_crowd_threshold()
        life_span = self.__rand_lifespan()

        fish = FishData(id, genesis, pheromone_threshold,
                        crowd_threshold, life_span, parent_id)
        return fish

    def __rand_id(self) -> str:
        "returns a random 6 digit string"
        id = ""
        for _ in range(6):
            id += "0123456789"[math.floor(random.random() * 10)]
        return id

    def __rand_pheromone_threshold(self) -> int:
        return random.randint(30, 60)

    def __rand_crowd_threshold(self) -> int:
        return random.randint(5, 20)

    def __rand_lifespan(self) -> int:
        """
        returns a random value between 60 and 120 with 99% probability,
        and returns 0 with 1% probability.
        """
        return 0 if random.random() <= 0.01 else random.randint(60, 120)
