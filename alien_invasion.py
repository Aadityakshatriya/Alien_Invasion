import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
     #initialising the ship, and pygame
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #make a ship
    ship = Ship(ai_settings= ai_settings, screen = screen)

    #make a group to store bullets in
    bullets = Group()

    #make an alien
    alien = Alien(ai_settings,screen)

#start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        #Get rid of old bullets
        gf.update_bullets(bullets)

        #update the screen with the newest frame
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()