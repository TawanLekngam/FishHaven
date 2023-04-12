import config
from Pond import Pond
from Storage import Storage


def main():
    storage = Storage(config.REDIS_HOST, config.REDIS_PORT, config.REDIS_PASSWORD, config.REDIS_DB)
    p = Pond(config.POND_NAME, storage)
    p.run()


if __name__ == "__main__":
    main()
