from gamelib.util import *

"""
"""
class Character(object):
    
    def __init__(self):
        self.hp = 0
        self.name = "Nameless Thingy"
        self.items = []
        self.px = 0
        self.py = 0
        self.armour = 0
        self.spirit = 0
        self.agility = 0
        
class Player(Character):
    
    def __init__(self):
        Character.__init__(self)
        self.hp = 25
        self.name = "Explorer1"
        
    def Generate(self):
        self.items.append("Dagger")

if __name__ == "__main__":
    p = Player()
