from gamelib.util import *
from gamelib.symbols import *

"""
Generate a square cave map.
"""
class CaveGenerator(object):

    def __init__(self, width, defaultc = 0):
        self.cave = [ defaultc for i in range(width * width) ]
        self.width = width
        self.spaces = []
        self.diamond = True
    def setc(self, x, y, v):
        self.cave[ (y * self.width) + x] = v
        if MAINROUTE==v: 
            if not (x,y) in self.spaces:
                self.spaces.append( (x,y) )
        if self.diamond:self.cave[ -1 ] = DIAMOND
    def getc(self, x, y):
        p = (y * self.width) + x
        if p >= len(self.cave) or p<0:
            return 0
        return self.cave[ p ]
        
    def getneigh(self, x, y):
        rl = []
        rl.append(self.getc(x-1, y-1))
        rl.append(self.getc(x, y-1))
        rl.append(self.getc(x+1, y-1))
        rl.append(self.getc(x-1, y))
        rl.append(self.getc(x+1, y))
        rl.append(self.getc(x-1, y+1))
        rl.append(self.getc(x, y+1))
        rl.append(self.getc(x+1 ,y+1))
        return rl
        
    def getneighm(self, x, y):
        rl = []
        rl.append([ x-1, y-1, self.getc(x-1, y-1) ])
        rl.append([ x, y-1, self.getc(x, y-1) ])
        rl.append([ x+1, y-1, self.getc(x+1, y-1) ])
        rl.append([ x-1, y, self.getc(x-1, y) ])
        rl.append([ x+1, y, self.getc(x+1, y) ])
        rl.append([ x-1, y+1, self.getc(x-1, y+1) ])
        rl.append([ x, y+1, self.getc(x, y+1) ])
        rl.append([ x+1 ,y+1, self.getc(x+1 ,y+1) ])
        rrl=[]
        for n in rl:
            if (n[2]>2000 and n[2]<3000):
                rrl.append(n)
        print(rrl)
        return rrl
        
    def setRect(self, x, y, w, h, c):
        for xr in range(x , x + w):
            for yr in range(y, y + h):
                self.setc(xr, yr, c)

    def Generate(self):
        sx = 0
        sy = 0
        ex = self.width - 1
        ey = self.width - 1
        for i in range(5 + RND(5) ):
            self.MakeRoute(sx, sy, ex, ey)
        
        # Place Diamond
        self.setc(ex, ey, DIAMOND)
        
        # Baddies
        placed = False
        #while !placed:
        sc = len(self.spaces)
        cx = ( sc // 2) + RND(len(self.spaces) // 4)
        
        #self.setc(pos[0], pos[1], NINJA)
        bads = len(self.spaces) // (self.width//3)
        print("adding " + str(bads))
        for bg in range(bads):
            pos = self.spaces[ RND(sc) ]
            while pos[0]<5 and pos[1]<5:
                pos = self.spaces[ RND(sc) ]
            m =  2001 + RND(MAXMON)
            self.setc(pos[0], pos[1],m)
        
        food = self.width//5 +  RND(5)
        for ng in range(food):
            pos = self.spaces[ RND(sc) ]
            if self.getc(pos[0], pos[1]) == 1:
                self.setc(pos[0], pos[1], APRICOT)
        for ng in range(self.width*2):
            x = RND(self.width)
            y = RND(self.width)
            if self.getc(x, y) == 0:
                self.setc(x, y, GOLDORE)
                print("Gold")
    def MakeRoute(self, sx, sy, ex, ey):
        self.setc(sx, sy, MAINROUTE)
        while sx!=ex or sy!=ey:
            if sx!=ex:
                nextpath = RND(8)
                if sx+nextpath>ex: nextpath = ex-sx
                for i in range(nextpath):
                    sx += 1
                    self.setc(sx, sy, MAINROUTE)
            if sy!=ey:
                nextpath = RND(8)
                if sy+nextpath>ey: nextpath = ey-sy
                for i in range(nextpath):
                    sy += 1
                    self.setc(sx, sy, MAINROUTE)
        
    def Show(self):
        for x in range(self.width):
            line = ""
            for y in range(self.width):
                line += str(self.getc(x,y))
            print(line)
        
if __name__ == "__main__":
    cg = CaveGenerator(64)
    cg.Generate()
    cg.Show()
