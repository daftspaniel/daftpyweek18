from gamelib.util import *

MAINROUTE = 1

"""
Generate a square cave map.
"""
class CaveGenerator(object):

    def __init__(self, width):
        self.cave = [ 0 for i in range(width * width) ]
        self.width = width
        
    def setc(self, x, y, v):
        self.cave[ (y * self.width) + x] = v
        
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
