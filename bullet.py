import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_setting,screen,ship):
        super().__init__()
        self.ai_setting   = ai_setting
        self.screen       = screen
        self.ship         = ship
        self.rect         = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top     = ship.rect.top
        self.y            = float(self.rect.y)
        self.color        = self.ai_setting.bullet_color
        self.speed_factor = self.ai_setting.bullet_speed_factor

    def update(self):            # Function to update the position of the bullet
        self.y           -= self.ai_setting.bullet_speed_factor
        self.rect.y       = self.y

    def draw_bullet(self):       # Function to draw the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
