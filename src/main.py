import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "true"


from Pond import Pond
from Storage import Storage, connect_to_redis




def main():
    r = connect_to_redis()
    storage = Storage(r)
    p = Pond("doo-pond", storage)
    p.run()


if __name__ == "__main__":
    main()
