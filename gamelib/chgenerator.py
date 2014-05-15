from gamelib.util import *
from gamelib.symbols import *

"""
"""
sagelines = [
                "Watch out for my evil brothers!",
                "Blue is faster than Tuesday!",
                "Don't get out much...",
                "Who planted these trees?",
                "Times change.",
                "Selfie!",
                "42",
                "I Haz the wisdom",
                "Onion is out today",
                "Follow daftspaniel on Twitter",
                ""
            ]
            
def getCharSpeaks(character):
    if character==SAGE:
        return "THE SAGE SAYS " + chr(34) + sagelines[RND( len(sagelines)-1 )] + chr(34) 

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
        self.level = 1
        self.exp = RND(5)
        
    def Generate(self):
        self.items.append("Dagger")

if __name__ == "__main__":
    p = Player()
