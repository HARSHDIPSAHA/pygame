import pygame
import random
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load("image/download.jpg")
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.right=random.randint(self.rect.width,self.screen_rect.width-self.rect.width)
        self.rect.top=random.randint(0,self.screen_rect.height-self.rect.height)
        self.y=float(self.rect.y)
        

    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        
        if self.y<= self.screen_rect.height:
            self.y+=0.4
            self.rect.y=self.y

    
            
                

            
        
        
    
