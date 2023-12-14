import pygame
import gf
from pygame.sprite import Group
from ak47 import Ak
def RunGame():
    pygame.init()
    pygame.display.set_caption("LOL")
    screen=pygame.display.set_mode((1200,800))
    ak=Ak(screen)
    
    while True:
        
        
        gf.key_events(screen,ak)
        
        ak.update()
        ak.blitme()
        gf.fill(screen)
        
        

RunGame()
        
        
