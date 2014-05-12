from gamelib.util import *

MAINROUTE = 1
DIAMOND = 1001

NINJA = 2001

"""
Generate a square cave map.
"""
class CaveGenerator(object):

    def __init__(self, width):
        self.cave = [ 0 for i in range(width * width) ]
        self.width = width
        self.spaces = []
        
    def setc(self, x, y, v):
        self.cave[ (y * self.width) + x] = v
        if MAINROUTE==v: 
            self.spaces.append( (x,y) )
        
    def getc(self, x, y):
        if ((y * self.width) + x) >= len(self.cave):
            return 0
        return self.cave[ (y * self.width) + x]

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
        cx = (len(self.spaces) // 2) + RND(len(self.spaces) // 4)
        pos = self.spaces[cx]
        self.setc(pos[0], pos[1], NINJA)
            
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
