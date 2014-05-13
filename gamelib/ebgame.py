from gamelib.dgenerator import *
from gamelib.chgenerator import *
from gamelib.util import *
from gamelib.gfxstore import *

class EBGame(object):
    """
        Main game class.
    """
    def __init__(self, surface, screen):
        self.Location = 2
        self.surface = surface
        self.screen = screen
        self.scale = 64
        self.gfx = gfxStore(self.scale)
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
        #self.cg.Show()
        #self.cur = self.cg
        
    def CreateRooms(self):
        self.home = CaveGenerator(12, HOMEFLOOR)
        self.cur = self.home
        self.home.setc(9, 9, PORTAL)
    def MainLoop(self):
        #
        self.UpdateScreen()
            
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
                        if self.p1.px>self.cur.width:
                            self.p1.px = self.cur.width
                        if self.p1.py>self.cur.width:
                            self.p1.py = self.cur.width
                        if self.cur.getc(self.p1.px, self.p1.py)==0:
                            self.p1.px = oldx
                            self.p1.py = oldy
                        else:
                            self.UpdateScreen()
                            self.UpdateSFX()
                            self.sfx.step.play()
                                
    
    def UpdateScreen(self):

        self.surface.fill(pygame.Color("grey"))
        
        #if self.Location == 2:
        #    self.DrawHome()
        #elif self.Location == 1:
        #    self.DrawCave()
        self.DrawRoom()
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
        
    def UpdateSFX(self):
        c = self.cur.getc(self.p1.px, self.p1.py)
        if c == DIAMOND:
            self.sfx.found.play()
        elif c == PORTAL:
            self.sfx.portal.play()
        
    def DrawHome(self):
        self.surface.fill(pygame.Color("blue"))
        DrawText8(self.surface, 8, 8, "You are at home.")
        
        for x in range(0, 8):
            for y in range(0, 8):
                c = self.home.getc(x,y)
                p = Rect( x * self.scale, y * self.scale, self.scale , self.scale)
                if c==0:
                     self.surface.blit(self.gfx.wfloor, p )
        
    def DrawRoom(self):
        
        w = self.cur.width
        sx = max(self.p1.px - 4, 0)
        sy = max(self.p1.py - 4, 0)
        ex = min(w, sx + 16)
        ey = min(w, sy + 16)
        
        # Draw The Required Tiles
        for x in range(sx, ex):
            for y in range(sy, ey):
                c = self.cur.getc(x,y)
                p = Rect( x * self.scale, y * self.scale, self.scale , self.scale)
                p[0] -= self.scale * (self.p1.px - 4 )
                p[1] -= self.scale * (self.p1.py -4 )
                if c == 1:
                     self.surface.blit(self.gfx.floor, p )
                elif c == 0:
                     self.surface.blit(self.gfx.block, p )
                elif c == HOMEFLOOR:
                    self.surface.blit(self.gfx.wfloor, p )
                elif c == PORTAL:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.portal1, p )
                    if RND(3)==1:
                        self.surface.blit(self.gfx.portal2, p )
                        
                elif c == DIAMOND:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.diamond, p )
                elif c == NINJA:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.ninja, p )
        
        # Status Area
        pygame.draw.rect(self.surface, pygame.Color("white"), Rect(0,450,800,150) )
        pygame.draw.rect(self.surface, pygame.Color("black"), Rect(0,450,800,149), 1 )
        DrawText8(self.surface, 8, 458, "Hero :" + str(self.p1.name) )
        
        self.surface.blit(self.gfx.player, (4 * self.scale, 4 * self.scale, self.scale, self.scale) )
        for h in range(0,8):
            self.surface.blit(self.gfx.heart, (8 +(8*h), 490, 8, 8) )
