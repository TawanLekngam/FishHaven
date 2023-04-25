import pickle
import sys
import time
from typing import List

import redis

import config
from factories import fishFactory
from FishSprite import FishSprite
from Log import get_logger

log = get_logger("redis")


class Storage:
    RETRIES = 3
    INITIAL_INTERVAL = 1
    BACKOFF_FACTOR = 2

    def __init__(self, host="localhost", port=6379, password: str = None, db: int = 0):
        self.host = host
        self.port = port
        self.password = password
        self.redis: redis.StrictRedis = None
        interval = Storage.INITIAL_INTERVAL

        for i in range(Storage.RETRIES):
            try:
                self.redis = redis.StrictRedis(
                    host=host, port=port, password=password, db=db)
                if self.redis.ping():
                    log.info(f"Connected to Redis at {host}:{port}")
                    break
                else:
                    raise redis.ConnectionError()

            except redis.ConnectionError:
                if i < Storage.RETRIES - 1:
                    log.warning(
                        f"Failed to connect to Redis at {host}:{port}, retrying in {interval} seconds")
                    time.sleep(interval)
                    interval *= Storage.BACKOFF_FACTOR
                else:
                    log.error(
                        f"Failed to connect to Redis at {host}:{port}, after {Storage.RETRIES} attempts")
                    sys.exit(-1)

    def add_fish(self, fish: FishSprite):
        id = fish.get_id()
        data = fish.get_data()
        time_left = data.get_lifespan() - data.get_age()
        if time_left <= 0:
            time_left = 0 if data.get_lifespan() != 0 else None
        self.redis.set(id, pickle.dumps(data), ex=time_left)

    def remove_fish(self, ids: list[str]):
        self.redis.delete(*ids)

    def get_fishes(self) -> List[FishSprite]:
        fishes_ids = self.redis.keys()

        fishes_data = []
        for data in self.redis.mget(fishes_ids):
            if data is not None:
                fish_data = pickle.loads(data)
                fishes_data.append(fish_data)

        fishes_sprite = []
        for fish_data in fishes_data:
            fish_sprite = fishFactory.generate_fish_by_data(fish_data)
            fishes_sprite.append(fish_sprite)

        return fishes_sprite


if __name__ == "__main__":
    storage = Storage()
