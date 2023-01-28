import pygame
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Fish Haven")

    clock = pygame.time.Clock()
    running = True

    while (running):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((175, 215, 70))
        pygame.display.update()
        clock.tick(120)


if __name__ == "__main__":
    main()
