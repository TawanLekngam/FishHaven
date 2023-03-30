import random

from Entity import Entity, Direction
from FishData import FishData
from movements import Movement


class FishSprite(Entity):

    def __init__(self, data: FishData, movement: Movement):
        self.data = data
        self.movement = movement

        self.frame = 0
        self.direction = random.choice([Direction.LEFT, Direction.RIGHT])

        self.time_in_pond = 0

    def get_id(self):
        return self.data.get_id()

    def get_genesis(self):
        return self.data.get_genesis()

    def get_parent_id(self):
        return self.data.get_parent_id()

    def get_state(self):
        return self.data.get_state()

    def is_pregnant(self):
        if self.data.get_pheromone() >= self.data.get_pheromone_threshold():
            self.reset_pheromone()
            return True
        return False

    def is_immortal(self):
        return self.data.get_lifespan() == 0

    def is_alive(self):
        return self.is_immortal() or self.data.get_lifespan() > self.data.get_age()

    def add_pheromone(self, amount: float):
        self.data.set_pheromone(self.data.get_pheromone() + amount)

    def reset_pheromone(self):
        self.data.set_pheromone(0)

    def die(self):
        self.get_state("dead")
        self.kill()

    def get_data(self):
        return self.data

    def update(self):
        self.__update_time()
        self.__update_sprite()
        self.movement.move(self)

    def __update_sprite(self):
        self.frame = (self.frame + 1) % len(self.sprites[self.direction])
        self.image = self.sprites[self.direction][int(self.frame)]

    def __update_time(self):
        self.time_in_pond += 1
        if self.is_immortal():
            return

        self.data.set_age(self.data.get_age() + 1)
