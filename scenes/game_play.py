from core.scene import Scene
from states.game import game_states
from data.languages import languages
from core.functions import get_language, world_debug
from game.entities.ground.ground import Ground
from core.components.skybox import SkyBox
from game.entities.player.player import Player
from panda3d.core import *
from game.lights.light import *
from game.entities.test import Test

class GamePlay(Scene):
    def __init__(self):
        super().__init__()
        self.scene_name = 'game_play'
        self.a_light = None
        self.d_light = None
        self.p_light = None
        
    def config(self):
        # world_debug()
        pass
        
    def create(self):
        super().create()
        self.config()
        self.objects['a_light'] = ambient_light()
        self.objects['d_light'] = directional_light()
        self.objects['sky'] = SkyBox()
        self.objects['ground'] = Ground()
        self.objects['player'] = Player()
        self.objects['test'] = Test()

    def update(self, dt):
        self.objects['player'].update(dt)
        self.objects['test'].update(dt)