import pygame
import time
from setting import Settings
import game_functions as gf
from ship import Ship
def run_game():
    # Here initialising pygame, settings, and screen object   
    pygame.init()
    ai_sett = Settings()
    screen = pygame.display.set_mode((ai_sett.screen_width,ai_sett.screen_height))
    pygame.display.set_caption('Alien invasion')
    ship = Ship(screen,ai_sett)
    
    while True:
        gf.check_events(ship)                 # Function to check for events        
        gf.update_screen(ai_sett,screen,ship) # Function to update the screen
        
run_game()
