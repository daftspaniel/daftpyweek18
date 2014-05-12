import random
import pygame
from pygame.locals import *

ANIMEVENT = pygame.USEREVENT+3
DAYEVENT = pygame.USEREVENT+4
GameTitle  = "8-bit RPG"

fontgfx = pygame.image.load("img/font.png").convert()
fontgfx.set_colorkey((255, 255, 255))

def RND(maxv):
    return random.randrange(0, maxv)
    

def CreateSurface(screen):
    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    #bg.set_colorkey((255, 255, 255))
    return bg

def DrawText(bg, x, y, text, size=24, color=(255, 255, 255)):
    inst1_font = pygame.font.Font(None, size)
    inst1_surf = inst1_font.render(text, 1, color)
    bg.blit(inst1_surf, [x, y])


def DrawText8(bg, x, y, text):
    text = text.upper()
    for c in text:
        #print(ord(c)-65)   
        lsx = (ord(c)-65) * 8
        #print((lsx,0,8,8))
        bg.blit(fontgfx, (x,y,8,8) , (lsx,0,8,8) )
        x += 8
