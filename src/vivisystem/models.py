from enum import Enum

from typing import NamedTuple


class EventType(str, Enum):
    CONNECT = 1
    DISCONNECT = 2
    STATUS = 3
    MIGRATE = 4

class VivisystemPond(NamedTuple):
    name: str
    total_fishes: int = 0
    pheromone: float = 0

class VivisystemFish(NamedTuple):
    fish_id: int
    parent_id: int
    genesis: str
    crowd_threshold: int
    pheromone_threshold: int
    lifetime: int