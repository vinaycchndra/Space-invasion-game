import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_setting,screen):
        super().__init__()
        self.ai_setting = ai_setting
        self.screen     = screen
        self.image      = pygame.image.load('images/alien.bmp')
        self.rect       = self.image.get_rect()
        self.rect.x     = self.rect.width
        self.rect.y     = self.rect.height
        # making x a floar variable
        self.x          = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
