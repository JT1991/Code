import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats

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
    #Create instance to store game statistics
    stats = GameStats(ai_settings)
    
    #Start main loop for game
    while True:
        #Watch for keyboard/mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        #Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
