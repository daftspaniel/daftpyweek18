from gamelib.util import *

"""
"""
class Player(object):
    
    def __init__(self):
        self.hp = 12
        self.name = "Player1"
        self.items = []
        self.px = 0
        self.py = 0
        
    def Generate(self):
        self.items.append("Dagger")

if __name__ == "__main__":
    p = Player()
