from pickle import dumps, loads
from redis import Redis, ConnectionError
from time import sleep
from typing import List

from model import FishModel


RETRIES = 3
INTERVAL = 1
BACKOFF_FACTOR = 2


class Storage:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.redis: Redis = None

    def connect(self):
        interval = INTERVAL
        for i in range(RETRIES):
            try:
                self.redis = Redis(host=self.host, port=self.port)
                if self.redis.ping():
                    print(f"Connected to {self.host}:{self.port}")
                    break
                else:
                    raise ConnectionError()
            except ConnectionError:
                if i < RETRIES - 1:
                    print(f"Failed to connect retrying in {interval} seconds")
                    sleep(interval)
                    interval *= BACKOFF_FACTOR
                else:
                    print(f"Failed to connect after {RETRIES} attempts")

    def disconnect(self):
        if self.redis:
            self.redis.close()
            print(f"Disconnected from {self.host}:{self.port}")

    def retrieveAll(self) -> List[FishModel]:
        models = []
        for key in self.redis.keys():
            data = self.redis.get(key)
            model = loads(data)
            models.append(model)
        return models

    def store(self, model: FishModel):
        id = model.id
        data = dumps(model)
        self.redis.set(id, data)

    def delete(self, id: str):
        self.redis.delete(id)

    def deleteAll(self):
        self.redis.flushall()

    def backup(self, filename: str):
        with open(filename, "wb") as file:
            for key in self.redis.keys():
                data = self.redis.get(key)
                file.write(data)

    def restore(self, filename: str):
        with open(filename, "rb") as file:
            data = file.read()
            self.redis.set("backup", data)


if __name__ == "__main__":
    storage = Storage("localhost", 6379)
    storage.connect()
    storage.disconnect()
