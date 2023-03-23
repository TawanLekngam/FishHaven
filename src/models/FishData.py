from datetime import datetime


class FishData:

    def __init__(self, id: str, genesis: str, pheromone_threshold: int, crowd_threshold: int, life_span: int = 60, parent_id: str = None):
        self.id = id
        self.genesis = genesis
        self.parent_id = parent_id
        self.state = "in-pond"
        self.crowd_threshold = crowd_threshold
        self.pheromone = 0
        self.pheromone_threshold = pheromone_threshold
        self.life_span = life_span
        self.is_immortal = life_span == 0
        self.birth_date = datetime.now()
        self.time_in_pond = 0

    def get_id(self):
        return self.id

    def get_genesis(self):
        return self.genesis

    def get_parent_id(self):
        return self.parent_id

    def get_pheromone_threshold(self):
        return self.pheromone_threshold
    
    def get_crowd_threshold(self):
        return self.crowd_threshold

    def get_pheromone(self):
        return self.pheromone

    def get_life_span(self):
        return self.life_span

    def get_state(self):
        return self.state

    def is_alive(self):
        """Check if fish is alive"""
        if self.is_immortal:
            return True
        return (datetime.now() - self.birth_date).seconds < self.life_span

    def get_life_left(self):
        """Get remaining life in seconds"""
        if self.is_immortal:
            return float("inf")
        return self.life_span - (datetime.now() - self.birth_date).seconds

    def update(self):
        if self.state == "dead":
            return

        self.time_in_pond += 1

        if self.is_immortal:
            return

        if datetime.now() - self.birth_date > self.life_span:
            self.state = "dead"

    def migrate(self):
        self.state = "migrating"
        self.time_in_pond = 0
