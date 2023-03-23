import pickle
import sys
import redis
import time


from logging import getLogger

from models import FishData, FishSprite
from scripts.movement import BounceMovement

log = getLogger("redis")


def connect_to_redis(host="localhost", port=6379, password=None, retries=3, retry_interval=1) -> redis.StrictRedis:
    for i in range(retries):
        try:
            r = redis.StrictRedis(host=host,
                                  port=port,
                                  password=password)
            if r.ping():
                log.info(f"connected to Redis at {host}:{port}")
                return r
            else:
                raise redis.ConnectionError()

        except redis.ConnectionError:
            if i < retries - 1:
                log.warning(
                    f"failed to connect to Redis at {host}:{port}, retrying in {retry_interval} second")
                time.sleep(retry_interval)
            else:
                log.error(
                    f"failed to connect to Redis at {host}:{port}, after {retries} attempts")
                sys.exit(-1)


class Storage:
    def __init__(self, target_redis):
        self.redis: redis.StrictRedis = target_redis

    def add_fish(self, fish: FishData):
        """Add a fish to the redis database"""
        try:
            self.redis.set(fish.get_id(), pickle.dumps(
                fish), ex=fish.get_life_left())
        except redis.exceptions.ResponseError:
            log.error("failed to add fish to redis")

    def remove_fish(self, ids: list[str]):
        self.redis.delete(*ids)

    def get_fishes(self):
        """Get all fishes from the redis database"""
        fishes_ids = self.redis.keys()
        fishes_data = [
            pickle.loads(data) for data in self.redis.mget(fishes_ids) if data is not None
        ]

        fishes_sprite = [FishSprite(fish_data, BounceMovement(3))
                         for fish_data in fishes_data]
        return dict(zip(fishes_ids, fishes_sprite))
