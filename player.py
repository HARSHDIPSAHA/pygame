import pygame
class Player:
    def __init__(self,screen):
        self.screen=screen
        self.image=pygame.image.load("image/player.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.ml=False
        self.mr=False
        self.life=3

    def update(self):
        if self.ml and self.rect.x>0:
            self.rect.x-=1.5
        elif self.mr and self.rect.right< self.screen_rect.width:
            self.rect.x+=1.5

        


    def blitme(self):
        self.screen.blit(self.image,self.rect)
    
