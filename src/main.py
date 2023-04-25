import config
from Pond import Pond
from Storage import Storage
from vivisystem import VivisystemClient


def main():
    storage = Storage(config.REDIS_HOST, config.REDIS_PORT,
                      config.REDIS_PASSWORD, config.REDIS_DB)
    client = VivisystemClient(config.VIVISYSTEM_URL, config.POND_NAME)
    p = Pond(config.POND_NAME, storage, client)
    p.run()


if __name__ == "__main__":
    main()
