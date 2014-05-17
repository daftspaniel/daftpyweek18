import time

from gamelib.dgenerator import *
from gamelib.chgenerator import *
from gamelib.util import *
from gamelib.gfxstore import *

class Arena(object):
    """
        Main game class.
    """
    def __init__(self, eb, monster):
        self.surface = eb.surface
        self.screen = eb.screen
        
        self.eb = eb
        self.player1 = eb.p1
        self.monster = monster
        self.bigmonster = pygame.transform.scale(self.eb.gfx.monsters[self.monster], (350, 450) )
        self.player = pygame.transform.scale(self.eb.gfx.player, (350, 450) )
        self.bigfloor = pygame.transform.scale(self.eb.gfx.floor, (800, 450) )
        self.CreateMonster()
        self.LastAttack = -1
        self.LastMonsterAttack = -1
        
    def CreateMonster(self):
        self.e1 = Character()
        if self.monster==NINJA: self.e1.init( "Ninja", 1, 9, 2,  2, 8, 8 )
        if self.monster==SPIDER: self.e1.init( "Spider", 1, 8, 3, 2, 7, 9 )
        if self.monster==HEDGE: self.e1.init( "Veg Monster", 1, 7, 4, 1, 3, 3 )
        if self.monster==SNAKE: self.e1.init( "Snake", 1, 6, 5, 2, 7, 8 )
        if self.monster==BLOB: self.e1.init( "Blob", 1, 5, 6, 2, 4, 6 )
        if self.monster==GHOST: self.e1.init( "Ghost", 1, 5, 7, 1, 9, 4 )
        if self.monster==PHANTOM: self.e1.init( "Phantom", 1, 5, 8, 1, 9, 4 )
        if self.monster==SNAIL: self.e1.init( "Snail", 1, 4, 1, 2, 1, 2 )
        if self.monster==EVILSAGE: self.e1.init( "Evil Sage", 1, 9, 7, 1, 3, 5 )
        if self.monster==DRAGON: self.e1.init( "Dragon", 1, 50, 12, 12, 12, 12 )
        
    def MainLoop(self):
        
        #while self.player.hp>0:
        self.UpdateScreen()
        Fighting = True
        while Fighting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    
                    if keystate[K_g]==1:
                        self.e1.hp = 1
                    if keystate[K_f]==1:
                        self.LastAttack = self.player1.getAttack() 
                        self.LastMonsterAttack = self.e1.getAttack() 
                        self.e1.defend(self.LastAttack, False)
                        if self.e1.hp>0:
                            self.player1.defend(self.LastMonsterAttack)
                        
                        self.eb.sfx.tap.play()
                        time.sleep(1)
                        self.UpdateScreen()
                        
                        if self.e1.hp<1:
                            self.eb.sfx.win.play()
                            Fighting = False
                            return 1
                        if self.player1.hp<1:
                            self.eb.sfx.lose.play()
                            Fighting = False
                            return 0
    def DrawArena(self):

        if self.monster!=DRAGON:
            self.surface.blit( self.player, (10, 10) )
            self.surface.blit( self.bigmonster, (400, 10) )
        else:
            player = pygame.transform.scale(self.eb.gfx.player, (64, 64) )
            dragon = pygame.transform.scale(self.eb.gfx.dragon, (600, 300) )
            
            self.surface.blit( dragon, (150, 100) )
            self.surface.blit( player, (10, 360) )
        pygame.draw.rect(self.surface, pygame.Color("white"), Rect(0,450,800,150) )
        pygame.draw.rect(self.surface, pygame.Color("black"), Rect(0,450,800,148), 1 )
        
        ph = self.player1.heartCount()
        eh = self.e1.heartCount()
        
        DrawText8(self.surface, 8, 458, "NAME :" + str(self.player1.name) )
        DrawText8(self.surface, 8, 476, "HP :" + str(self.player1.hp) )
        
        if self.LastAttack != -1:
            if self.LastAttack>0:
                DrawText8(self.surface, 208, 476, "YOU ATTACK " + str(self.LastAttack) )
            else:
                DrawText8(self.surface, 208, 476, "You miss!")
            
            if self.LastMonsterAttack>0:
                DrawText8(self.surface, 208, 490,  self.e1.name + " ATTACKS " + str(self.LastMonsterAttack) )
            else:
                DrawText8(self.surface, 208, 490,  self.e1.name + " MISS " )
        
        for h in range(0,10):
            if h<ph:
                self.surface.blit(self.eb.gfx.heart, (8 +(16*h), 518, 8, 8) )
            else:
                self.surface.blit(self.eb.gfx.greyheart, (8 +(16*h), 518, 8, 8) )
        
        DrawText8(self.surface, 508, 458, "NAME :" + str(self.e1.name) )
        DrawText8(self.surface, 508, 476, "HP :" + str(self.e1.hp) )

        for h in range(0,10):
            if h<eh:
                self.surface.blit(self.eb.gfx.heart, (508 +(16*h), 518, 8, 8) )
            else:
                self.surface.blit(self.eb.gfx.greyheart, (508 +(16*h), 518, 8, 8) )

    def UpdateScreen(self):

        self.surface.fill(pygame.Color("white"))
        self.surface.blit(self.bigfloor, (0,0))
        self.DrawArena()
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
