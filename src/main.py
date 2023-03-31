from Pond2 import Pond
from Storage import Storage


def main():
    storage = Storage()
    p = Pond("doo-pond", storage)
    p.run()


if __name__ == "__main__":
    main()
