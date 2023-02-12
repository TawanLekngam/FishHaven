import pickle
import redis
import time


from typing import List, Union
from logging import getLogger

from models.Fish import Fish
from FishSprite import FishSprite

log = getLogger("redis")


def connect_to_redis(host="localhost", port=6379, password=None, retries=5, retry_interval=1, db=0) -> Union[redis.StrictRedis, None]:
    for i in range(retries):
        try:
            r = redis.StrictRedis(host=host,
                                  port=port,
                                  password=password,
                                  db=db)
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
                return None


class Storage:
    def __init__(self, target_redis):
        self.redis: redis.StrictRedis = target_redis

    def add_fish(self, fish: Fish): 
        self.redis.set(fish.get_id(), pickle.dumps(fish), ex=fish.get_lifespan())

    def remove_fish(self, ids: List[str]):
        self.redis.delete(*ids)

    def get_fishes(self):
        fishes_ids = self.redis.keys()
        fishes_data = [
            pickle.loads(data) for data in self.redis.mget(fishes_ids) if data is not None
        ]

        fishes_sprite = [FishSprite(fish_data) for fish_data in fishes_data]
        return dict(zip(fishes_ids, fishes_sprite))
