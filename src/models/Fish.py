class Fish:
    _instances = {}

    def __new__(
        cls,
        id: str,
        genesis: str,
        gender: str,
        pheromone_threshold: int,
        crowd_threshold: int,
        lifespan: int,
        parent_id: str = None
    ):
        if id not in cls._instances:
            cls._instances[id] = super().__new__(cls)
        return cls._instances[id]

    def __init__(
            self,
            id: str,
            genesis: str,
            gender: str,
            pheromone_threshold: int,
            crowd_threshold: int,
            lifespan: int,
            parent_id: str = None
    ):
        if not hasattr(self, "id"):
            self.id = id
            self.genesis = genesis
            self.parent_id = parent_id
            self.gender = gender
            self.pheromone_threshold = pheromone_threshold
            self.crowd_threshold = crowd_threshold
            self.pheromone = 0
            self.lifespan = lifespan
            self.time_in_pond = 0
            self.state = "in-pond"
            self.is_alive = True
            self.is_immortal = lifespan == 0

    def __str__(self):
        return f"ID:{self.id} | Gender:{self.gender} | Parent ID:{self.parent_id}"

    def get_id(self):
        return self.id

    def get_genesis(self):
        return self.genesis

    def get_lifespan(self):
        return self.lifespan

    def inject_pheromone(self, amount: int):
        if self.gender == "male":
            return
        self.pheromone += amount
        if self.pheromone > 100:
            self.pheromone = 0


if __name__ == "__main__":
    f1 = Fish("001", "pond", "male", 1, 1, 1)
    f2 = Fish("002", "pond", "male", 1, 1, 1)
    f3 = Fish("001", "pond", "female", 1, 1, 1)
    f2.gender = "female"
    print(f1)
    print(f2)
    print(f3)
