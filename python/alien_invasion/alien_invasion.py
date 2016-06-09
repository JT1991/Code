import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize pygame, settings, screen and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #make ship
    ship = Ship(ai_settings ,screen)
    #Make a group to store bullets in
    bullets = Group()
    #Make an alien group
    aliens = Group()

    #Create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Start main loop for game
    while True:
        #Watch for keyboard/mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        #Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
