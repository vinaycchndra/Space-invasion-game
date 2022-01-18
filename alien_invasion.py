import sys
import pygame
import time
from setting import Settings
def run_game():
    # Here initialising pygame, settings, and screen object   
    pygame.init()
    ai_sett = Settings()
    screen = pygame.display.set_mode((ai_sett.screen_width,ai_sett.screen_height))
    pygame.display.set_caption('Alien invasion')
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(ai_sett.bg_color)
        pygame.display.flip()
        
run_game()
