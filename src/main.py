import pygame
from Pond import Pond
from Storage import Storage, connect_to_redis




def main():
    pygame.init()
    pygame.display.set_caption("Doo Pond")
    pygame.display.set_mode((1280, 720))
    r = connect_to_redis()
    storage = Storage(r)
    p = Pond("doo-pond", storage)
    p.run()


if __name__ == "__main__":
    main()
