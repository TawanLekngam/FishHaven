from Pond2 import Pond
from Storage import Storage

import config


def main():
    storage = Storage()
    p = Pond(config.POND_NAME, storage)
    p.run()


if __name__ == "__main__":
    main()
