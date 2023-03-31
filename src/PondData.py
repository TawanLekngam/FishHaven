from typing import Dict

from FishData import FishData


class PondData:
    def __init__(self, name: str):
        self.name = name
        self.fishes: Dict[str, FishData] = {}

    def get_name(self):
        return self.name

    def get_population(self):
        return len(self.fishes)

    def add_fish(self, fish: FishData):
        self.fishes[fish.get_id()] = fish

    def get_fish_by_id(self, id: str) -> FishData:
        return self.fishes[id]

    def remove_fish(self, id: str):
        self.fishes.pop(id, None)

    def get_fishes(self) -> Dict[str, FishData]:
        return self.fishes
