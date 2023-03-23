from pygame.sprite import Group

from collections import defaultdict
from typing import Callable, DefaultDict, Dict
from .FishSprite import FishSprite


class FishGroup(Group):

    FISH_DISPLAY_LIMIT = 100

    def __init__(self):
        super().__init__()
        self.fishes: DefaultDict[str,
                                 Dict[str, FishSprite]] = defaultdict(dict)

    def add_fish(self, fish: FishSprite):
        self.fishes[fish.get_genesis()][fish.get_id()] = fish
        print(self.fishes.keys(), "add_fishes")
        if self.get_total() < self.FISH_DISPLAY_LIMIT:
            self.add(fish)

    def remove_fish(self, fish: FishSprite):
        if fish.get_genesis() in self.fishes:
            self.fishes[fish.get_genesis()].pop(fish.get_id(), None)

    def update_fishes(self, update: Callable[[FishSprite], None]):
        for genesis in self.fishes.keys():
            for fish_id, fish in dict(self.fishes[genesis]).items():
                print("update_fishes", fish_id)
                update(fish)


    def get_total(self):
        return sum([len(self.fishes[k]) for k in self.fishes.keys()])

    def get_fish(self, genesis: str = "doo-pond"):
        fishes = []
        for fish in self.fishes[genesis].values():
            fishes.append(fish)
        return fishes
