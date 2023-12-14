from settings import Setting
from ship import Ship
import game_functions as gf
import pygame
from pygame.sprite import Group
from gamestats import Gamestats

#from alien import Alien
def run_game():
  pygame.init()
  ai_setting=Setting()
  screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height ))
  ship=Ship(screen,ai_setting)
  pygame.display.set_caption("Alien Invasion")
  bullets=Group()
  stats=Gamestats(ai_setting)
  #alien=Alien(ai_setting,screen)
  aliens=Group()
  gf.create_fleet(ai_setting, screen, aliens,ship)
  

  while True:
      gf.check_events(ai_setting,screen,ship,bullets)
      if stats.active:
        gf.update_bullets(ai_setting,screen,aliens,ship,bullets)
        ship.update()
        gf.update_aliens(ai_setting,aliens,screen,ship,stats,bullets)
        gf.alien_hit(stats,aliens,screen,ai_setting,ship,bullets)
        
      for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
          bullets.remove(bullet)
      gf.update_screen(ai_setting,screen,ship,bullets,aliens)
         
      

run_game()
