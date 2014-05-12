from gamelib.util import *

class gfxStore(object):

    def __init__(self, scale):
        self.scale = scale
        self.player = self.LoadGFX("img/player.png")
        
        # Scene
        self.block = self.LoadGFX("img/scene/stone.png") 
        self.floor = self.LoadGFX("img/scene/floor.png")
        self.chest = self.LoadGFX("img/scene/chest.png")
        self.brick = self.LoadGFX("img/scene/brick.png")
        self.mush = self.LoadGFX("img/scene/mush.png")
        self.shrub = self.LoadGFX("img/scene/shrub.png")
        self.wfloor = self.LoadGFX("img/scene/wfloor.png")
        
        # Items
        self.diamond = self.LoadGFX("img/items/diamond.png")
        self.heart = self.LoadGFX("img/items/heart.png")
        
        # Enemies
        self.ninja = self.LoadGFX("img/baddies/ninja.png")
        self.blob = self.LoadGFX("img/baddies/blob.png")
        self.ghost = self.LoadGFX("img/baddies/ghost.png")
        self.phantom = self.LoadGFX("img/baddies/phantom.png")
        self.snail = self.LoadGFX("img/baddies/snail.png")
        self.snake = self.LoadGFX("img/baddies/snake.png")
        self.spider = self.LoadGFX("img/baddies/spider.png")
        self.veg = self.LoadGFX("img/baddies/veg.png")
        
        # NPC
        self.duck = self.LoadGFX("img/npc/duck.png")
        self.llama = self.LoadGFX("img/npc/llama.png")
        
    def LoadGFX(self, filename):
        i = pygame.image.load(filename).convert()
        i.set_colorkey((255, 255, 255))
        return pygame.transform.scale(i, (self.scale, self.scale))


class sfxStore(object):

    def __init__(self):
        self.step = self.LoadSND("snd/step.wav")
        self.found = self.LoadSND("snd/coin.wav")
    def LoadSND(self, filename):
        return pygame.mixer.Sound(filename)
