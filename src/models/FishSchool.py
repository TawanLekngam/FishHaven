from pygame.sprite import Group

from collections import defaultdict
from typing import Callable, DefaultDict, Dict
from .FishSprite import FishSprite


class FishSchool(Group):

    FISH_DISPLAY_LIMIT = 100

    def __init__(self):
        super().__init__()
        self.fishes: DefaultDict[str,Dict[str, FishSprite]] = defaultdict(dict)

    def add_fish(self, fish: FishSprite):
        self.fishes[fish.get_genesis()][fish.get_id()] = fish
        if self.get_total() < self.FISH_DISPLAY_LIMIT:
            self.add(fish)

    def remove_fish(self, fish: FishSprite):
        if fish.get_genesis() in self.fishes:
            self.fishes[fish.get_genesis()].pop(fish.get_id(), None)

    def update_fishes(self, update: Callable[[FishSprite], None]):
        for genesis in self.fishes.keys():
            for _, fish in dict(self.fishes[genesis]).items():
                update(fish)

    def update(self, *args):
        """Update the fish school. If the number of fish is less than the limit"""
        super().update(*args)
        if len(self.sprites()) < self.FISH_DISPLAY_LIMIT:
            for genesis_fishes in self.fishes.values():
                for fish in genesis_fishes.values():
                    if len(self.sprites()) < self.FISH_DISPLAY_LIMIT and fish not in self.sprites():
                        self.add(fish)


    def get_total(self):
        return sum([len(self.fishes[k]) for k in self.fishes.keys()])

    def get_fish(self, genesis: str = "doo-pond"):
        fishes = []
        for fish in self.fishes[genesis].values():
            fishes.append(fish)
        return fishes
