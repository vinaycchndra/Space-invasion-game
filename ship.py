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
        self.moving_right = False
        self.moving_left  = False

    def update(self):
        if self.moving_right==True:
            self.rect.centerx+=1

        if self.moving_left==True:                           # Here we are not using the elif condition since it will check only only one true event and 
            self.rect.centerx-=1                             # it will make ship moving only to the left thus by using both if we can check if both are 
                                                             # the ship addition and subtraction will happen one after another             
        
    def blitme(self):
        self.screen.blit(self.img,self.rect)                  # Method to place ship image on the screen that was taken as output for this class in the main space_invasion.py file


       
