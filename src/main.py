from Storage import Storage, connect_to_redis
from Pond import Pond

def main():
    r = connect_to_redis()
    storage = Storage(r)
    p = Pond("doo-pond", storage)
    p.run()


if __name__ == "__main__":
    main()
