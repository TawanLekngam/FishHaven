import math
import random


def rand_id():
    "returns a random 6 digit numeric."
    id = ""
    for _ in range(6):
        id += "0123456789"[math.floor(random.random() * 10)]
    return id


def rand_crowd_thresh():
    return random.randint(5, 20)


def rand_pheromone_thresh():
    return random.randint(30, 60)


def rand_life_thresh():
    """
    returns a random value between 60 and 120 with 99% probability,
    and returns 0 with 1% probability.
    """
    return 0 if random.random() <= 0.01 else random.randint(60, 120)


class FishData:
    def __init__(self, genesis: str, parent_id: str = None):
        self.id = rand_id()
        self.genesis = genesis
        self.parent_id = parent_id
        self.gender = random.choice(["male", "female"])

        self.threshold_of_pheromone = rand_pheromone_thresh()
        self.threshold_of_crowd = rand_crowd_thresh()
        self.threshold_of_life = rand_life_thresh()

        self.pheromone = 0
        self.lifetime = self.threshold_of_life
        self.time_in_pond = 0
        self.state = "in-pond"
        self.is_alive = True
        self.is_immortal = False if self.threshold_of_life != 0 else True

    def __str__(self):
        return f"id:{self.id} gender:{self.gender} parent id:{self.parent_id}"

    def get_id(self):
        return self.id
