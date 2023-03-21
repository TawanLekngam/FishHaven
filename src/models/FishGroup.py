from pygame.sprite import Group

from collections import defaultdict
from typing import Callable, DefaultDict, Dict
from .FishSprite import FishSprite


class FishGroup(Group):

    FISH_DISPLAY_LIMIT = 300

    def __init__(self):
        super().__init__()
        self.fishes: DefaultDict[str,
                                 Dict[str, FishSprite]] = defaultdict(dict)

    def add_fish(self, fish: FishSprite):
        self.fishes[fish.get_genesis()][fish.get_id()] = fish
        if self.get_total() < self.FISH_DISPLAY_LIMIT:
            self.add(fish)

    def update_fish(self, update: Callable[[FishSprite], None]):
        for genesis in self.fishes.keys():
            for fish in self.fishes[genesis].values():
                update(fish)

    def get_total(self):
        return sum([len(self.fishes[k]) for k in self.fishes.keys()])

    def get_fish(self, genesis: str = "doo-pond"):
        fishes = []
        for fish in self.fishes[genesis].values():
            fishes.append(fish)
        return fishes
