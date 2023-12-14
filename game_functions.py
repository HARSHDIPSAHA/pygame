import sys
import pygame
from bullet import Bullet
from alien import Alien
from gamestats import Gamestats
from time import sleep

def fire_bullet(ai_setting, screen, ship, bullets):
    if len(bullets)<ai_setting.bullets_allowed:
                new_bullet=Bullet(ai_setting,screen,ship)
                bullets.add(new_bullet) 

def check_keydown_events(ai_setting,screen,bullets,event, ship):
            
        if event.key == pygame.K_RIGHT:
            ship.moving_right=True
        elif event.key == pygame.K_LEFT:
            ship.moving_left=True
        elif event.key==pygame.K_SPACE:
            fire_bullet(ai_setting, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()
    
def check_keyup_events(event, ship):
    
    if event.key==pygame.K_RIGHT:
            
        ship.moving_right=False
    elif event.key == pygame.K_LEFT:
        ship.moving_left=False
def check_events(ai_setting,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_setting,screen,bullets,event, ship)
             
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def get_row(ai_setting,alien_height,ship_height):
    v_space=ai_setting.screen_height- (3*alien_height)-ship_height
    numrow= int(v_space/(2*alien_height))
    return numrow

def get_alien_numx(ai_setting, alien_width):
    av_space=ai_setting.screen_width-(2*(alien_width))
    alien_numx=int(av_space/(2*alien_width))
    return alien_numx
def create_alien(ai_setting, screen, aliens, alien_number,row_number):
    alien=Alien(ai_setting,screen)
    alien_width=alien.rect.width
    alien.x= alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+(2*row_number*alien.rect.height)
    aliens.add(alien)
    

    
def create_fleet(ai_setting,screen,aliens,ship):
    alien=Alien(ai_setting,screen)
    alien_numx=get_alien_numx(ai_setting, alien.rect.width)
    numrow=get_row(ai_setting,alien.rect.width,ship.rect.height)
   
        
    for row_number in range(numrow):
        
        for alien_number in range(alien_numx):
             
            create_alien(ai_setting, screen, aliens, alien_number,row_number)
                  
def update_screen(ai_setting,screen,ship,bullets,aliens):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():        
        bullet.draw_bullets()

    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(ai_setting,screen,aliens,ship,bullets):
    bullets.update()
    get_collison(ai_setting,screen,aliens,ship,bullets)
    

def get_collison(ai_setting,screen,aliens,ship,bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens)==0:
        bullets.empty()
        create_fleet(ai_setting,screen,aliens,ship)
        ai_setting.alien_speedf+=0.5
    
def update_aliens(ai_setting,aliens,screen,ship,stats,bullets):
    check_fleet_edges(ai_setting,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        
        ship_hit(ai_setting,aliens,ship,stats,bullets,screen)
def ship_hit(ai_setting,aliens,ship,stats,bullets,screen):
    if stats.liferem>1:
        stats.liferem-=1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setting,screen,aliens,ship)
        ship.centre_ship()
        sleep(0.5)
    else:
        stats.active=False


        
        
def alien_hit(stats,aliens,screen,ai_setting,ship,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom>=screen_rect.height:
            ship_hit(ai_setting,aliens,ship,stats,bullets,screen)
            break
        

def check_fleet_edges(ai_setting,aliens):
    for alien in aliens.sprites():
        if alien.edge():
            change_direction(ai_setting,aliens)
            break



    
def change_direction(ai_setting,aliens):
    ai_setting.direction*=-1
    for alien in aliens.sprites():
        alien.rect.y+=ai_setting.down_speed
    
    
