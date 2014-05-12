from gamelib.util import *

class gfxStore(object):

    def __init__(self):
        self.pgfx = self.LoadGFX("img/player.png")
        self.block = self.LoadGFX("img/scene/stone.png") 
        self.floor = self.LoadGFX("img/scene/floor.png")

    def LoadGFX(self, filename):
        i = pygame.image.load(filename).convert()
        i.set_colorkey((255, 255, 255))
        return pygame.transform.scale(i, (self.scale, self.scale))


class sfxStore(object):

    def __init__(self):
        self.step = self.LoadSND("snd/step.wav")
    def LoadSND(self, filename):
        return pygame.mixer.Sound(filename)
