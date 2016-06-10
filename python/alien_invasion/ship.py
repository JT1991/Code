import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        """Intialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        #Load ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start new ship at bottom centre
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store decimal value for ships centre
        self.center = float(self.rect.centerx)
        
        #Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ships position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def center_ship(self):
        """Centre the ship on the screen"""
        self.center = self.screen_rect.centerx
        

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
