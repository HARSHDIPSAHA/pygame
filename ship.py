import pygame
class Ship:
    def __init__(self,screen,ai_setting):
        self.screen=screen
        self.image = pygame.image.load('images/rock.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
        self.ai_setting=ai_setting
        self.center=float(self.rect.centerx)
        

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.ai_setting.speed_factor

        elif self.moving_left and self.rect.left > 0:
            self.center-=self.ai_setting.speed_factor

        self.rect.centerx=self.center
    def centre_ship(self):
        self.center=self.screen_rect.centerx
