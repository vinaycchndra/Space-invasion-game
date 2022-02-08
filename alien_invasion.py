import pygame
import time
from pygame.sprite import Group
from setting import Settings
import game_functions as gf
from ship import Ship
from alien import Alien
def run_game():
    #Here initialising pygame, settings, and screen object   
    pygame.init()
    ai_sett    = Settings()
    screen     = pygame.display.set_mode((ai_sett.screen_width,ai_sett.screen_height))
    pygame.display.set_caption('Alien invasion')
    ship       = Ship(screen,ai_sett)
    bullets    = Group()
    alien      = Alien(ai_sett,screen)
    while True:
        gf.check_events(ai_sett,screen,ship,bullets)        # Function to check for events        
        ship.update()                                       # Method which updates the ship movement from keys input    
        gf.update_bullets(bullets)                          # Update bullet positions      
        gf.update_screen(ai_sett,screen,ship,bullets,alien) # Function to update the screen
        
run_game()
