import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    
    ai_settings = Settings()

    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #bg_color = (230, 230, 230)
    ship = Ship(screen)

#start the main loop for the game
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

#fill the screen with bg_color
        screen.fill(ai_settings.bg_color)
        ship.blitme()

#make the most recently drawn screen visible
        pygame.display.flip()

run_game()
    