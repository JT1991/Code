import pygame
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
    ship = Ship(screen)
    
    #Start main loop for game
    while True:
        #Watch for keyboard/mouse events
        gf.check_events(ship)
        #Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, ship)

run_game()
