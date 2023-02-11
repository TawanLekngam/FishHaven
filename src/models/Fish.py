
class Fish:
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
