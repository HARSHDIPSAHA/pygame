import pygame
from pygame.sprite import Sprite
from ak47 import Ak
import sys
def fill(screen):
    screen.fill((230,230,230))
    pygame.display.flip()

def key_events(screen,ak):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        
        
        elif event.type==pygame.KEYDOWN:
            
            key_down(event,ak)
        elif event.type==pygame.KEYUP:   
            key_up(event,ak)
            
def key_up(event,ak):
    if event.key==pygame.K_UP:
        ak.ismovingup=False

    elif event.key==pygame.K_DOWN:
        ak.ismovingdown=False       

def key_down(event,ak):
    if event.key==pygame.K_UP:
        ak.ismovingup=True
    elif event.key==pygame.K_DOWN:
        ak.ismovingdown=True
        
        
        
    
    


    
