from gamelib.dgenerator import *
from gamelib.chgenerator import *
from gamelib.util import *
from gamelib.gfxstore import *

class EBGame(object):
    """
        Main game class.
    """
    def __init__(self, surface, screen):
        self.Location = 1
        self.surface = surface
        self.screen = screen
        self.scale = 64
        self.gfx = gfxStore()
        self.sfx = sfxStore()
        #key init
        self.p1 = Player()
        
    def LoadGFX(self, filename):
        i = pygame.image.load(filename).convert()
        i.set_colorkey((255, 255, 255))
        return pygame.transform.scale(i, (self.scale, self.scale))
        
    def StartCave(self):
        self.cg = CaveGenerator(64)
        self.cg.Generate()
        self.cg.Show()
        
    def MainLoop(self):
        print("ml")
        self.DrawHome()
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
        print("ml")
        #while True:
        #    if self.Location == 1:
        #        pass
        
        self.DrawCave()
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    keystate = pygame.key.get_pressed()
                    
                    oldx = self.p1.px
                    oldy = self.p1.py
                    
                    if keystate[K_d]==1:
                        self.p1.px += 1
                    elif keystate[K_a]==1:
                        self.p1.px -= 1
                    elif keystate[K_w]==1:
                        self.p1.py -= 1
                    elif keystate[K_s]==1:
                        self.p1.py += 1

                    if oldx != self.p1.px or oldy != self.p1.py:
                        if self.p1.px<0: self.p1.px = 0 
                        if self.p1.py<0: self.p1.py = 0
                        if self.p1.px>self.cg.width:
                            self.p1.px = self.cg.width
                        if self.p1.py>self.cg.width:
                            self.p1.py = self.cg.width
                        if self.cg.getc(self.p1.px, self.p1.py)==0:
                            self.p1.px = oldx
                            self.p1.py = oldy
                        else:
                            self.Update()
                            self.sfx.step.play()
    
    def Update(self):
        print(self.p1.px)
        print(self.p1.py)
        self.surface.fill(pygame.Color("grey"))
        self.DrawCave()
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
        
    def DrawHome(self):
        DrawText8(self.surface, 8, 8, "You are at home.")
        
    def DrawCave(self):
        w = self.cg.width
        sx = max(self.p1.px - 4, 0)
        sy = max(self.p1.py - 4, 0)
        ex = min(self.cg.width, sx + 16)
        ey = min(self.cg.width, sy + 16)
        for x in range(sx, ex):
            for y in range(sy, ey):
                c = self.cg.getc(x,y)
                p = Rect( x * self.scale, y * self.scale, self.scale , self.scale)
                p[0] -= self.scale * (self.p1.px - 4 )
                p[1] -= self.scale * (self.p1.py -4 )
                if c==1:
                     #pygame.draw.rect(self.surface, pygame.Color("brown"), p )
                     self.surface.blit(self.floor, p )
                if c==0:
                     self.surface.blit(self.block, p )
        pygame.draw.rect(self.surface, pygame.Color("white"), Rect(0,450,800,150) )
        DrawText8(self.surface, 8, 458, "you are in the dungeon.")
        
        self.surface.blit(self.pgfx, (4 * self.scale, 4 * self.scale, self.scale, self.scale) )
