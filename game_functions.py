import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.rect.centerx+=1

            elif event.key==pygame.K_LEFT:
                ship.rect.centerx-=1
                

def update_screen(ai_sett,screen,ship):
    screen.fill(ai_sett.bg_color)
    ship.blitme()                # Method which plots ship image on the screen
    pygame.display.flip()
    
    
