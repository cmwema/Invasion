import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represents a single alien in the fleet"""
    
    def __init__(self, ai_settings, screen):
        """initialize the alien and set its start position"""
        
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien image and load its rect attribute
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

        

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen.rect.right:
            return True

        elif self.rect.left <= 0:
            return True


    def update(self):
        """move the alien right or left"""

        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
