from collections import defaultdict
from typing import Callable, Dict, List

from pygame.sprite import Group

from FishSprite import FishSprite


class FishSchool(Group):
    RENDER_LIMIT = 100

    def __init__(self):
        Group.__init__(self)
        self.__fishes: Dict[str, Dict[str, FishSprite]] = defaultdict(dict)

    def add_fish(self, fish: FishSprite):
        self.__fishes[fish.get_genesis()][fish.get_id()] = fish
        if self.get_population() < self.RENDER_LIMIT:
            self.add(fish)

    def remove_fish(self, fish: FishSprite):
        if fish.get_genesis() in self.__fishes:
            self.__fishes[fish.get_genesis()].pop(fish.get_id(), None)

        if fish in self.sprites():
            self.sprites().remove(fish)

    def update_data(self, update: Callable[[FishSprite], None]):
        for genesis in self.__fishes.keys():
            for _, fish in dict(self.__fishes[genesis]).items():
                update(fish)

    def update_sprite(self, *args, **kwargs):
        super().update(*args, **kwargs)
        if len(self.sprites()) >= self.RENDER_LIMIT:
            return

        for genesis_fishes in self.__fishes.values():
            for fish in genesis_fishes.values():
                if len(self.sprites()) < self.RENDER_LIMIT and fish not in self.sprites() and fish.is_alive():
                    self.add(fish)

    def get_population(self, genesis: str = None):
        if genesis:
            return len(self.__fishes[genesis])
        return sum([len(self.__fishes[k]) for k in self.__fishes.keys()])

    def get_fishes(self):
        fishes: List[FishSprite] = []
        for genesis in self.__fishes.keys():
            for fish in self.__fishes[genesis].values():
                fishes.append(fish)
        return fishes

    def get_genesis(self):
        return list(self.__fishes.keys())

    def get_fishes_by_genesis(self, genesis: str):
        fishes: List[FishSprite] = []
        for fish in self.__fishes[genesis].values():
            fishes.append(fish)
        return fishes

    def get_items(self):
        return self.__fishes.items()
