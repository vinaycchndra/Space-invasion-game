import sys
import pygame
from bullet import Bullet
from alien import Alien

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

    elif event.key == pygame.K_q:                                   #Game exiting with q pressing 
            pygame.quit()
            sys.exit()

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

def update_screen(ai_sett,screen,ship,bullets,aliens):
    screen.fill(ai_sett.bg_color)
    ship.blitme()                                                   #Method which plots ship image on the screen
    aliens.draw(screen)                                             #Method which plots alien image on the screen
    for bullet in bullets.sprites():   
        bullet.draw_bullet()
    pygame.display.flip()

def create_fleet(ai_setting,screen,aliens):                         #Alien fleet create function
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    total_space = ai_setting.screen_width-2*alien_width             #Number of aliens that can sit in the screen
    Number_of_aliens = total_space//(2*alien_width)
    for _ in range(Number_of_aliens):                               #adding aliens to the group object
        alien = Alien(ai_setting, screen)
        alien.x = alien_width*(1+2*_)
        alien.rect.x = alien.x
        aliens.add(alien)















    
    
    
        
    
