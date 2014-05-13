'''
Game main module.
'''

import sys
import pygame

pygame.init()
ScreenSize = [800,600]
screen = pygame.display.set_mode(ScreenSize)

from pygame.locals import *
from gamelib.util import *
from gamelib.ebgame import *

pygame.display.set_caption(GameTitle)
pygame.time.set_timer(ANIMEVENT, 2000)

surface = CreateSurface(screen)
Game = None

#------
# MAIN
#------
def main():
    
    GameState = 1
    surface.fill(pygame.Color("white"))
    DrawText8(surface, 10, 50, "Daftspaniel Presents...")#, 48, (255,255,255) )
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    while GameState!=-1:

        if GameState == 1:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == ANIMEVENT:
                    surface.fill(pygame.Color("white"))
                    DrawText8(surface, 10, 50, GameTitle)#, 48, (255,0,0) )
                    DrawText8(surface, 11, 51, GameTitle)#, 48, (255,156,0) )
                    DrawText8(surface, 11, 51, GameTitle)#, 48, (255,255,255) )

                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_SPACE]:
                        GameState = 2
                    if keystate[K_ESCAPE]==1:
                        GameState = -1

            screen.blit(surface, (0, 0))
            pygame.display.flip()
            
        elif GameState == 2: 
            
            surface.fill(pygame.Color("black"))
            
            DrawText8(surface, 10, 50, "Please Wait...")
            screen.blit(surface, (0, 0))
            pygame.display.flip()
            Game = EBGame(surface, screen)
            Game.CreateRooms()
            #Game.StartCave()
            surface.fill(pygame.Color("black"))
            GameState = 3
            
        elif GameState == 3:
            surface.fill(pygame.Color("blue"))
            screen.blit(surface, (0, 0))
            pygame.display.flip()
            while GameState == 3:
                Game.MainLoop()
                GameState = 4
            
        elif GameState == 4:
            
            print("Game over")
            surface.fill(pygame.Color("black"))
            DrawText(surface, 10, 50, "Game Over", 48, (255,0,0) )
            
            while GameState == 4:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        keystate = pygame.key.get_pressed()
                        if keystate[K_SPACE]:
                            GameState = 1
                    elif event.type == ANIMEVENT:
                        screen.blit(surface, (0, 0))
                        pygame.display.flip()

        elif GameState == 5: # Game Win

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == ANIMEVENT:
                    surface.fill(pygame.Color("black"))
                    DrawText(surface, 10, 50, "Well Done!", 48, (255,0,0) )
                    
                elif event.type == pygame.KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    if keystate[K_SPACE]:
                        GameState = 1
                        
            screen.blit(GameBG, (0, 0))
            pygame.display.flip()
