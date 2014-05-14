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
        self.p1.px = 1
        self.p1.py = 1
        self.TEXT = "Test"
        
    def LoadGFX(self, filename):
        i = pygame.image.load(filename).convert()
        i.set_colorkey((255, 255, 255))
        return pygame.transform.scale(i, (self.scale, self.scale))
        
    def StartCave(self):
        self.cg = CaveGenerator(64)
        self.cg.Generate()
        #self.cg.Show()
        self.cur = self.cg
        
    def CreateRooms(self):
        self.home = CaveGenerator(24, SHRUB)
        self.cur = self.home
        
        self.home.setRect(1, 1, 22, 22, MAINROUTE)
        self.home.setRect(0, 0, 8, 8, BRICK)
        self.home.setRect(15, 15, 8, 4, BRICK)
        self.home.setRect(1, 1, 6, 6, HOMEFLOOR)
        
        self.home.setRect(7, 4, 1, 1, DOOR)
        self.home.setRect(4, 4, 1, 1, CHEST)
        self.home.setRect(20, 4, 1, 1, DUCK)
        self.home.setRect(4, 21, 1, 1, LLAMA)
        self.home.setRect(8, 18, 1, 1, SAGE)
        
        self.home.setc(12, 9, PORTAL)
        
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
                        if self.cur.getc(self.p1.px, self.p1.py) in ( BRICK, 0):
                            self.p1.px = oldx
                            self.p1.py = oldy
                        else:
                            self.UpdateCharacters()
                            self.UpdateScreen()
                            self.UpdateSFX()
                            self.UpdateRoom()
                            self.sfx.step.play()
                                
    
    def UpdateScreen(self):

        self.surface.fill(pygame.Color("black"))
        
        self.DrawRoom()
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
        
    def UpdateSFX(self):
        c = self.cur.getc(self.p1.px, self.p1.py)
        if c == DIAMOND:
            self.sfx.found.play()
            self.sfx.portal.play()
        elif c == PORTAL:
            self.sfx.portal.play()
            
    def UpdateCharacters(self):
        
        self.TEXT = ""
        
        neighbouring = self.cur.getneigh(self.p1.px, self.p1.py)
        print(neighbouring)
        if SAGE in neighbouring:
            self.TEXT = "Watch out for my evil brothers!"
            
    def UpdateRoom(self):
        
        c = self.cur.getc(self.p1.px, self.p1.py)
        if c == PORTAL:
            self.StartCave()
            self.p1.px = 0
            self.p1.py = 0
            self.UpdateScreen()
        elif c == DIAMOND:
            self.cur = self.home
            self.p1.px = 7
            self.p1.py = 9
            self.UpdateScreen()
            
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
                elif c == BRICK:
                    self.surface.blit(self.gfx.brick, p )
                elif c == DOOR:
                    self.surface.blit(self.gfx.door, p )
                elif c == CHEST:
                    self.surface.blit(self.gfx.wfloor, p )
                    self.surface.blit(self.gfx.chest, p )
                elif c == SHRUB:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.shrub, p )
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
                    
                elif c == BLOB:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.blob, p )
                    
                elif c == EVILSAGE:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.evilsage, p )
                    
                elif c == GHOST:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.ghost, p )
                    
                elif c == PHANTOM:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.phantom, p )
                    
                elif c == SNAIL:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.snail, p )
                    
                elif c == SNAKE:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.snail, p )
                    
                elif c == HEDGE:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.veg, p )
                    
                elif c == DUCK:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.duck, p )
                    
                elif c == LLAMA:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.llama, p )
                elif c == SPIDER:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.spider, p )
                elif c == SAGE:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.sage, p )
                else:
                    print("!!!!!!!!!!!" + str(c) )
        
        # Status Area
        pygame.draw.rect(self.surface, pygame.Color("white"), Rect(0,450,800,150) )
        pygame.draw.rect(self.surface, pygame.Color("black"), Rect(0,450,800,148), 1 )
        DrawText8(self.surface, 8, 458, "NAME1 :" + str(self.p1.name) )
        DrawText8(self.surface, 144, 458, "HP :" + str(1234567890) )
        DrawText8(self.surface, 344, 458, self.TEXT )
        
        self.surface.blit(self.gfx.player, (4 * self.scale, 4 * self.scale, self.scale, self.scale) )
        for h in range(0,8):
            self.surface.blit(self.gfx.heart, (8 +(16*h), 490, 8, 8) )
