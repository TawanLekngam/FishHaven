class FishData:
    def __init__(self, id: str, genesis: str, pheromone_threshold: int, crowd_threshold: int, lifespan: int = 60, parent_id: str = None):
        self.id = id
        self.parent_id = parent_id
        self.genesis = genesis
        self.state = "in-pond"
        self.pheromone = 0
        self.pheromone_threshold = pheromone_threshold
        self.crowd_threshold = crowd_threshold
        self.age = 0
        self.lifespan = lifespan

    def get_id(self):
        return self.id

    def get_parent_id(self):
        return self.parent_id

    def get_genesis(self):
        return self.genesis

    def get_state(self):
        return self.state

    def get_pheromone(self):
        return self.pheromone

    def get_pheromone_threshold(self):
        return self.pheromone_threshold

    def get_crowd_threshold(self):
        return self.crowd_threshold

    def get_age(self):
        return self.age

    def get_lifespan(self):
        return self.lifespan

    def set_state(self, state: str):
        self.state = state

    def set_pheromone(self, pheromone: float):
        self.pheromone = pheromone

    def set_age(self, age: int):
        self.age = age
