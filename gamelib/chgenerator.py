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
                "I am sticking with Python 2 forever",
                "PyWeek FTW",
                "Somewhere be dragons",
                "Find those diamonds fast",
                "Orcs!",
                "LEGO Chima is quite cool.",
                ".......",
                "Have you read the fine manual?",
                "One day I will be in a real game.",
                "7",
                ""
            ]
            
def getCharSpeaks(character):
    if character==SAGE:
        return "THE SAGE SAYS " + chr(34) + sagelines[RND( len(sagelines)-1 )] + chr(34) 

class Character(object):
    
    def __init__(self):
        self.hp = 0
        self.maxhp = 0
        self.name = "Nameless Thingy"
        self.items = []
        self.px = 0
        self.py = 0
        self.armour = 0
        self.spirit = 0
        self.agility = 0
        self.gold = 0
        
    def init(self, name, level, hp, armour, spirit, agility, attack):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.armour = armour
        self.spirit = spirit
        self.agilit = agility
        self.attack = attack
        self.monster = True
        
    def heartCount(self):
        return int( 10 * (self.hp/self.maxhp) )

    def getAttack(self):
        a = RND(self.attack) + RND(self.spirit)
        if self.monster and self.hp<4:
            a = 1
        return a
        
        
    def defend(self, oppAttack, defend = True ):
        if defend:
            a = int( (oppAttack - ((self.armour + self.agility) / 5)) );
        else:
            a = oppAttack
        if a > 0: self.hp -= a;

class Player(Character):
    
    def __init__(self):
        Character.__init__(self)
        self.hp = 25
        self.init("Pythonista", 1, 25, 1, 1, 1, 4)
        self.exp = RND(5)
        self.level = 1
        self.diamonds = 0
        self.monster = False
        self.food = 0
        
    def Generate(self):
        self.items.append("Dagger")

if __name__ == "__main__":
    p = Player()
