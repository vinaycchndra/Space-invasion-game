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
            

def check_key_down_events(event,ship,screen,ai_setting,bullets):   #Function to check events of down key_press 
    if event.key==pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key==pygame.K_LEFT:
        ship.moving_left = True

    elif event.key==pygame.K_SPACE:
        fire_bullet(bullets,ai_setting,screen,ship)

def check_key_up_events(event,ship):                                #Function to check events of down key_press
    if event.key==pygame.K_RIGHT:
        ship.moving_right = False
                
    elif event.key==pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(bullets):
    bullets.update()                                                #Update the postition of group of bullets
    for old_bullet in bullets.copy():                               #Deletion of the bullets that have crossed the screen  
        if old_bullet.rect.bottom <= 0:
            bullets.remove(old_bullet)
    

def fire_bullet(bullets,ai_setting,screen,ship):                    #Function to fire the bullet
        if len(bullets)<ai_setting.bullets_allowed:                 #Condition to check the number of active bullets
            new_bullet = Bullet(ai_setting,screen,ship)
            bullets.add(new_bullet)    

def update_screen(ai_sett,screen,ship,bullets):
    screen.fill(ai_sett.bg_color)
    for bullet in bullets.sprites():   
        bullet.draw_bullet()
    ship.blitme()                                                   #Method which plots ship image on the screen
    pygame.display.flip()
        
    
