import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_setting,screen):
        super().__init__()
        self.ai_setting=ai_setting
        self.screen=screen
        self.image=pygame.image.load("images/alien.bmp")
        self.rect=self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        
        self.x+=(self.ai_setting.alien_speedf*self.ai_setting.direction)
        self.rect.x=self.x

    def edge(self):
        screen_rect=self.screen.get_rect()
        if self.rect.x>=screen_rect.width:
            return True

        elif self.rect.x<=0:
            return True

    
        
        
        
        
        

        
    
