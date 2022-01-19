import pygame
import matplotlib.pyplot as plt

class Ship():    
    def __init__(self,screen):
        self.screen = screen                                  # Screen on which we will set our image 
        self.img = pygame.image.load('images/ship_image.bmp') 
        self.rect = self.img.get_rect()                       # Rectangle surfce returned for the ship image to easily manipulate the coordinates 
        self.screen_rect = self.screen.get_rect()              
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        self.screen.blit(self.img,self.rect)                  # Method to place ship image on the screen that was taken as output for this class in the main space_invasion.py file


       
