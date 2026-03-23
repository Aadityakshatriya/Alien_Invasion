import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats

def run_game():
     #initialising the ship, and pygame
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #create an instance to store game statistics.
    stats = GameStats(ai_settings)

    #make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings= ai_settings, screen = screen)
    bullets = Group()
    aliens = Group()

    #create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

#start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()

            #Get rid of old bullets
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

            #update aliens
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

            #update the screen with the newest frame
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()