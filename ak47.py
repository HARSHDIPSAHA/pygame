import pygame
class Ak:
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("image/ak.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.midleft=self.screen_rect.midleft
        
        self.ismovingup=False
        self.ismovingdown=False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.rect.y>0 and self.ismovingup==True:
            self.rect.y-=1
        elif self.rect.y<self.screen_rect.height and self.ismovingdown==True:
            self.rect.y+=1
        
