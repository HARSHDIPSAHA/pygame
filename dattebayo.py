from settings import Setting
from naruto import Ship
import game_functions as gf
import pygame
def run_game():
  pygame.init()
  ai_setting=Setting()
  screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height ))
  ship=Ship(screen)
  pygame.display.set_caption("Ninja Way")

  while True:
      gf.check_events()
      gf.update_screen(ai_setting,screen,ship)
      
      

run_game()
