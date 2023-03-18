import math
import random
from models import Fish


class FishFactory:
    @staticmethod
    def generate_fish() -> Fish:
        "returns a Fish object with random properties"

        fish_id = FishFactory.__rand_id()
        genesis = 'doo-pond'
        gender = random.choice(['male', 'female'])
        pheromone_threshold = FishFactory.__rand_pheromone_threshold()
        crowd_threshold = FishFactory.__rand_crowd_threshold()
        lifespan = FishFactory.__rand_lifespan()

        fish = Fish(
            fish_id,
            genesis,
            gender,
            pheromone_threshold,
            crowd_threshold, lifespan
        )
        return fish

    @staticmethod
    def __rand_id() -> str:
        "returns a random 6 digit string"
        id = ""
        for _ in range(6):
            id += "0123456789"[math.floor(random.random() * 10)]
        return id

    @staticmethod
    def __rand_pheromone_threshold() -> int:
        return random.randint(30, 60)

    @staticmethod
    def __rand_crowd_threshold() -> int:
        return random.randint(5, 20)

    @staticmethod
    def __rand_lifespan() -> int:
        """
        returns a random value between 60 and 120 with 99% probability,
        and returns 0 with 1% probability.
        """
        return 0 if random.random() <= 0.01 else random.randint(60, 120)
