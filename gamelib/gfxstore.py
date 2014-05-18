from gamelib.util import *
from gamelib.symbols import *

import os

class gfxStore(object):

    def __init__(self, scale):
        self.scale = scale
        self.player = self.LoadGFX("img/player.png")
        
        # Scene
        self.block = self.LoadGFX("img/scene/stone.png") 
        self.stonegold = self.LoadGFX("img/scene/stonenug.png") 
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
        self.flower = self.LoadGFX("img/scene/flower.png", False)
        
        self.flower = pygame.transform.scale(self.flower, (16, 16))
        
        self.ftree = self.LoadGFX("img/scene/ftree.png")
        
        # Items
        self.diamond = self.LoadGFX("img/items/diamond.png")
        self.diamondsmall = self.LoadGFX("img/items/diamond.png", False)
        self.greydiamond = self.LoadGFX("img/items/greydiamond.png", False)
        self.heart = self.LoadGFX("img/items/heart.png", False)
        self.greyheart = self.LoadGFX("img/items/greyheart.png", False)
        self.apple = self.LoadGFX("img/items/apple.png")
        self.apricot = self.LoadGFX("img/items/apricot.png", False)
        
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
        
        self.fire = self.LoadGFX("img/baddies/fire.png")
        self.firedown = self.LoadGFX("img/baddies/firedown.png")
        
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
        self.monsters[DRAGON] = self.dragon
        # NPC
        self.duck = self.LoadGFX("img/npc/duck.png")
        self.llama = self.LoadGFX("img/npc/llama.png")
        self.sage = self.LoadGFX("img/npc/sage.png")
        self.farmer = self.LoadGFX("img/npc/farmer.png")
        self.shopkeeper = self.LoadGFX("img/npc/shopk.png")
        
    def LoadGFX(self, filename, scale = True):
        
        if filename.find(os.sep)==-1:
            filename = filename.replace("/", os.sep)
        
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
        self.tap = self.LoadSND("snd/tap.wav")
        self.win = self.LoadSND("snd/win.wav")
        self.lose = self.LoadSND("snd/lose.wav")
        
    def LoadSND(self, filename):
        if filename.find(os.sep)==-1:
            filename = filename.replace("/", os.sep)
        return pygame.mixer.Sound(filename)
