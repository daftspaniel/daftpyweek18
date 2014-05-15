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
        self.player = eb.p1
        self.eb = eb
        self.monster = monster
        self.bigmonster = pygame.transform.scale(self.eb.gfx.monsters[self.monster], (350, 450) )
        self.player = pygame.transform.scale(self.eb.gfx.player, (350, 450) )
        
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
                    Fighting = False
                    
    def DrawArena(self):

        self.surface.blit( self.player, (10, 10) )
        self.surface.blit( self.bigmonster, (400, 10) )
        
        pygame.draw.rect(self.surface, pygame.Color("white"), Rect(0,450,800,150) )
        pygame.draw.rect(self.surface, pygame.Color("black"), Rect(0,450,800,148), 1 )
        
    def UpdateScreen(self):

        self.surface.fill(pygame.Color("black"))
        
        self.DrawArena()
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
