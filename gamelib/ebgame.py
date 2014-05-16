import time

from gamelib.dgenerator import *
from gamelib.chgenerator import *
from gamelib.util import *
from gamelib.gfxstore import *
from gamelib.arena import *

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
        self.Status = []
        self.Status.append("Welcome to the game!")
        
    def AddStatus(self, status):
        self.Status.append(status)
        if len(self.Status)>4:
            self.Status = self.Status[1:]
    def ClearStatus(self):
        self.Status = []
    def LoadGFX(self, filename):
        i = pygame.image.load(filename).convert()
        i.set_colorkey((255, 255, 255))
        return pygame.transform.scale(i, (self.scale, self.scale))
        
    def StartCave(self):
        self.cg = CaveGenerator(64)
        self.cg.Generate()
        #self.cg.Show()
        self.cur = self.cg
        self.ClearStatus()
        self.AddStatus("YOU HAVE ENTERED THE DUNGEON")
        self.AddStatus("FIND THE DIAMOND TO EXIT")
        
    def CreateRooms(self):
        self.home = CaveGenerator(24, SHRUB)
        self.cur = self.home
        
        self.home.setRect(1, 1, 22, 22, GRASS)
        self.home.setRect(0, 0, 8, 8, BRICK)
        self.home.setRect(15, 15, 8, 4, BRICK)
        self.home.setRect(1, 1, 6, 6, HOMEFLOOR)
        
        self.home.setRect(8, 4, 9, 1, MAINROUTE)
        self.home.setRect(12, 5, 3, 3, MAINROUTE)
        
        self.home.setRect(7, 4, 1, 1, DOOR)
        self.home.setRect(4, 4, 1, 1, CHEST)
        
        self.home.setRect(17, 3, 5, 5, WATER)
        self.home.setRect(20, 4, 1, 1, DUCK)
        self.home.setRect(14, 4, 1, 1, LLAMA)
        self.home.setRect(12, 5, 1, 1, SAGE)
        
        self.home.setRect(11, 8, 4, 3, MAINROUTE)
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
                        if self.cur.getc(self.p1.px, self.p1.py) in ( WATER, BRICK, 0) or (self.cur.getc(self.p1.px, self.p1.py)>2000 and self.cur.getc(self.p1.px, self.p1.py)<3000):
                            
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
        
        self.PrevText = self.TEXT
        self.TEXT = ""
        c = self.cur.getc(self.p1.px, self.p1.py)
        neighbouring = self.cur.getneigh(self.p1.px, self.p1.py)
        #print(neighbouring)
        if SHRUB in neighbouring:
            self.AddStatus("The trees are very thick and tall.")
        if DUCK in neighbouring:
            self.AddStatus("QUACK.")
        if SAGE in neighbouring:
            self.TEXT = getCharSpeaks(SAGE)
            if self.PrevText != self.TEXT:
                self.AddStatus(self.TEXT)
                self.sfx.chat.play()
        if c == DOOR:
            self.AddStatus("This leads to the village.")
        if c == HOMEFLOOR:
            self.AddStatus("You are home.")
            
    def UpdateRoom(self):
        
        c = self.cur.getc(self.p1.px, self.p1.py)
        if c == PORTAL:
            self.StartCave()
            self.p1.px = 0
            self.p1.py = 0
            self.UpdateScreen()
        elif c == DIAMOND:
            self.cur = self.home
            self.p1.px = 4
            self.p1.py = 4
            self.UpdateScreen()
            
        #Fight
        monsters = self.cur.getneighm(self.p1.px, self.p1.py)
        if len(monsters)>0:
            mf = monsters[0]
            f = mf[2]
            if f>2000 and f<3000:
                print("Fight")
                #self.UpdateScreen()
                self.sfx.alarm.play()
                time.sleep(1)
                self.MonsterForFight = mf
                self.Fight(f) 
                
    def Fight(self, monster):
            self.surface.fill(pygame.Color("blue"))
            self.screen.blit(self.surface, (0, 0))
            pygame.display.flip()
            print("Fight start")
            print(self.MonsterForFight)
            fig = Arena(self, monster)  
            r = fig.MainLoop()
            if r==1:
                self.ClearStatus()
                self.AddStatus("Victory!")
                self.cur.setc(self.MonsterForFight[0], self.MonsterForFight[1], MAINROUTE)
                print(self.MonsterForFight)
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
        
        print("Updating Monsters")
        w = self.cur.width
        sx = max(self.p1.px - 4, 0)
        sy = max(self.p1.py - 4, 0)
        ex = min(w, sx + 16)
        ey = min(w, sy + 16)
        monsters = []
        for x in range(sx, ex):
            for y in range(sy, ey):        
                c = self.cur.getc(x,y)
                if c>2000 and c<3000:
                    monsters.append( [x,y] )
        cpf = self.cur.getc(self.p1.px, self.p1.py)
        self.cur.setc(self.p1.px, self.p1.py, WATER)#dummy
        
        for m in monsters:
            cm = self.cur.getc(m[0],m[1])
            #print(str(cm) + " " + str(m))
            vx = -1 if self.p1.px < m[0] else 1
            vy = -1 if self.p1.py < m[1] else 1
            #print(str(vx) + " " + str(vy))
            if self.cur.getc(m[0] + vx, m[1])==1:
                self.cur.setc(m[0] + vx, m[1], cm)
                self.cur.setc(m[0], m[1], 1)
            
            elif self.cur.getc(m[0], m[1] + vy)==1:
                self.cur.setc(m[0], m[1] + vy, cm)
                self.cur.setc(m[0], m[1], 1)
        
        self.cur.setc(self.p1.px, self.p1.py, cpf)#restore
        
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
                elif c == GRASS:
                    self.surface.blit(self.gfx.grass, p )
                elif c == WATER:
                    self.surface.blit(self.gfx.water, p )
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
                    #if RND(3)==1:
                    #    self.surface.blit(self.gfx.portal2, p )
                        
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
                    self.surface.blit(self.gfx.snake, p )
                    
                elif c == HEDGE:
                    self.surface.blit(self.gfx.floor, p )
                    self.surface.blit(self.gfx.veg, p )
                    
                elif c == DUCK:
                    self.surface.blit(self.gfx.water, p )
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
                DrawText8(self.surface, p[0], p[1], str(x) + "," + str(y) )
                    
        # Status Area
        pygame.draw.rect(self.surface, pygame.Color("white"), Rect(0,450,800,150) )
        pygame.draw.rect(self.surface, pygame.Color("black"), Rect(0,450,800,148), 1 )
        
        DrawText8(self.surface, 8, 458, "NAME :" + str(self.p1.name) )
        DrawText8(self.surface, 8, 476, "HP :" + str(self.p1.hp) )
        DrawText8(self.surface, 8, 489, "LEVEL :" + str(self.p1.level) )
        DrawText8(self.surface, 8, 502, "EXP :" + str(self.p1.level) )
        sy = 458
        for s in self.Status:
            sy += 12
            DrawText8(self.surface, 344, sy, s )
        
        self.surface.blit(self.gfx.player, (4 * self.scale, 4 * self.scale, self.scale, self.scale) )
        for h in range(0,10):
            if h<8:
                self.surface.blit(self.gfx.heart, (8 +(16*h), 518, 8, 8) )
            else:
                self.surface.blit(self.gfx.greyheart, (8 +(16*h), 518, 8, 8) )
            
