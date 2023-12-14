import pygame
import sys
from player import Player
import gf
from pygame.sprite import Group
from time import sleep
from ball import Ball

def run_game():
    pygame.init()
    pygame.display.set_caption("Catch")
    screen=pygame.display.set_mode((1200,800))
    player=Player(screen)
    if player.life>0:
        ball=Ball(screen) 
    #balls=Group()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                gf.key_down(event,player)

            elif event.type==pygame.KEYUP:
                gf.key_up(event,player)
        player.update()
        screen.fill((230,230,230))
        player.blitme()
        #gf.create_balls(balls,screen)
        #for ball in balls:
            #ball.update()
            #ball.blitme()
            #gf.update_balls(player,ball)
        if gf.update_balls(player,ball) or ball.rect.bottomleft[1]>=ball.screen_rect.height:    
            player.life-=1
            ball.rect.x=2000
        ball.update()
        ball.blitme()
        pygame.display.flip()
        
run_game()
          
        

    
