from .Fish import Fish


class PondData:
    def __init__(self, name: str):
        self.name = name
        self.fishes: dict[str, Fish] = {}

    def __str__(self):
        return f"{self.name} | {len(self.fishes)} fishes"

    def get_name(self):
        return self.name

    def get_population(self):
        return len(self.fishes)

    def add_fish(self, fish: Fish):
        self.fishes[fish.get_id()] = fish

    def get_fish_by_id(self, id: str):
        return self.fishes[id]

    def remove_fish(self, id: str):
        self.fishes.pop(id, None)

    def get_fishes(self):
        return self.fishes
    
