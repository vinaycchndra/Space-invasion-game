import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_screen(ai_sett,screen,ship):
    screen.fill(ai_sett.bg_color)
    ship.blitme()                # Method which plots ship image on the screen
    pygame.display.flip()
    
    
