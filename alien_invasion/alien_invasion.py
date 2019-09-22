import sys

import pygame

from settings import Settings

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1600, 900))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)

    while True:

        for event in pygame.event.get():
            screen.fill(bg_color)
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


run_game()
