import sys
import pygame
from bullet import Bullet
def check_events(ai_setting, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_key_down_events(event,ship,screen,ai_setting,bullets)
            

        elif event.type==pygame.KEYUP:
            check_key_up_events(event,ship)
            

def check_key_down_events(event,ship,screen,ai_setting,bullets):  #Function to check events of down key_press 
    if event.key==pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key==pygame.K_LEFT:
        ship.moving_left = True

    elif event.key==pygame.K_SPACE:
        new_bullet       = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullet)

def check_key_up_events(event,ship):    #Function to check events of down key_press
    if event.key==pygame.K_RIGHT:
        ship.moving_right = False
                
    elif event.key==pygame.K_LEFT:
        ship.moving_left = False
    

def update_screen(ai_sett,screen,ship,bullets):
    screen.fill(ai_sett.bg_color)
    ship.update()                       # Method which updates the ship movement from keys input
    for bullet in bullets.sprites():
        bullet.update()
        bullet.draw_bullet()
    ship.blitme()                       # Method which plots ship image on the screen
    pygame.display.flip()
        
    
