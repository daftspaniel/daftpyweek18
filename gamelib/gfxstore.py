from gamelib.util import *
from gamelib.symbols import *

class gfxStore(object):

    def __init__(self, scale):
        self.scale = scale
        self.player = self.LoadGFX("img/player.png")
        
        # Scene
        self.block = self.LoadGFX("img/scene/stone.png") 
        self.floor = self.LoadGFX("img/scene/floor.png")
        self.chest = self.LoadGFX("img/scene/chest.png")
        self.door = self.LoadGFX("img/scene/door.png")
        self.brick = self.LoadGFX("img/scene/brick.png")
        self.mush = self.LoadGFX("img/scene/mush.png")
        self.shrub = self.LoadGFX("img/scene/shrub.png")
        self.wfloor = self.LoadGFX("img/scene/wfloor.png")
        self.portal1 = self.LoadGFX("img/scene/portal1.png")
        self.portal2 = self.LoadGFX("img/scene/portal2.png")
        self.grass = self.LoadGFX("img/scene/grass.png")
        self.water = self.LoadGFX("img/scene/water.png")
        
        # Items
        self.diamond = self.LoadGFX("img/items/diamond.png")
        self.heart = self.LoadGFX("img/items/heart.png", False)
        self.greyheart = self.LoadGFX("img/items/greyheart.png", False)
        self.apple = self.LoadGFX("img/items/apple.png")
        self.apricot = self.LoadGFX("img/items/apricot.png")
        
        # Enemies
        self.ninja = self.LoadGFX("img/baddies/ninja.png")
        self.blob = self.LoadGFX("img/baddies/blob.png")
        self.ghost = self.LoadGFX("img/baddies/ghost.png")
        self.phantom = self.LoadGFX("img/baddies/phantom.png")
        self.snail = self.LoadGFX("img/baddies/snail.png")
        self.snake = self.LoadGFX("img/baddies/snake.png")
        self.spider = self.LoadGFX("img/baddies/spider.png")
        self.veg = self.LoadGFX("img/baddies/veg.png")
        self.evilsage = self.LoadGFX("img/baddies/evilsage.png")
        self.dragon = self.LoadGFX("img/baddies/dragon.png")
        self.monsters = {}
        self.monsters[NINJA] = self.ninja
        self.monsters[BLOB] = self.blob
        self.monsters[GHOST] = self.ghost
        self.monsters[PHANTOM] = self.phantom
        self.monsters[SNAIL] = self.snail
        self.monsters[SNAKE] = self.snake
        self.monsters[SPIDER] = self.spider
        self.monsters[HEDGE] = self.veg
        self.monsters[EVILSAGE] = self.evilsage
        # NPC
        self.duck = self.LoadGFX("img/npc/duck.png")
        self.llama = self.LoadGFX("img/npc/llama.png")
        self.sage = self.LoadGFX("img/npc/sage.png")
        
    def LoadGFX(self, filename, scale = True):
        i = pygame.image.load(filename).convert()
        i.set_colorkey((255, 255, 255))
        if scale:
            return pygame.transform.scale(i, (self.scale, self.scale))
        else:
            return i

class sfxStore(object):

    def __init__(self):
        self.step = self.LoadSND("snd/step.wav")
        self.found = self.LoadSND("snd/coin.wav")
        self.portal = self.LoadSND("snd/cyberpigeon.wav")
        self.chat = self.LoadSND("snd/chat.wav")
        self.alarm = self.LoadSND("snd/alarm.wav")
        
    def LoadSND(self, filename):
        return pygame.mixer.Sound(filename)
