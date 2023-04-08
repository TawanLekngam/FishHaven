import config
from Pond import Pond
from Storage import Storage


def main():
    storage = Storage()
    p = Pond(config.POND_NAME, storage)
    p.run()


if __name__ == "__main__":
    main()
