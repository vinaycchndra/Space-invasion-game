import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.moving_right = True

            elif event.key==pygame.K_LEFT:
                ship.moving_left = True

        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                ship.moving_right = False
                
            elif event.key==pygame.K_LEFT:
                ship.moving_left = False
                

def update_screen(ai_sett,screen,ship):
    screen.fill(ai_sett.bg_color)
    ship.update()
    ship.blitme()                # Method which plots ship image on the screen
    pygame.display.flip()
    
    
