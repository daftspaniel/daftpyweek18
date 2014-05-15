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
        if c=='1': lsx = 26 * 8
        elif c=='2': lsx = 27 * 8
        elif c=='3': lsx = 28 * 8
        elif c=='4': lsx = 29 * 8
        elif c=='5': lsx = 30 * 8
        elif c=='6': lsx = 31 * 8
        elif c=='7': lsx = 32 * 8
        elif c=='8': lsx = 33 * 8
        elif c=='9': lsx = 34 * 8
        elif c=='0': lsx = 35 * 8
        elif c=='"': lsx = 283
        #print((lsx,0,8,8))
        bg.blit(fontgfx, (x,y,8,8) , (lsx,0,8,8) )
        x += 8
