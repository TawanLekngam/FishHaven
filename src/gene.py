import random
import math
from abc import ABC, abstractmethod


class BaseGene(ABC):
    def __init__(self, genesis_pond: str = "doo-pond", parent_id: str = None):
        self.id: str = self.__rand_id()
        self.genesis_pond: str = genesis_pond
        self.parent_id: str = parent_id
        self.state: str = "in-pond"
        self.status: str = "alive"
        self.gender: str = random.choice(["male", "female"])
        self.time_in_pond: int = 0
        self.lifetime: int = random.randint(60, 120)

    def __rand_id(self) -> str:
        id = ""
        for _ in range(6):
            id += "0123456789"[math.floor(random.random() * 10)]
        return id

    def get_id(self) -> str:
        return self.id

    def get_genesis_pond(self) -> str:
        return self.genesis_pond
    
    def get_state(self) -> str:
        return self.state
    
    def get_status(self) -> str:
        return self.status

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError()