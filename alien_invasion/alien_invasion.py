import sys
import pygame
from .alien_invasion import Settings
from .alien_invasion import Ship

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:

        for event in pygame.event.get():
            screen.fill(ai_settings.bg_color)
            ship.blitme()
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


run_game()
