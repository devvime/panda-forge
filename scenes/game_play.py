from core.scene import Scene
from states.game import game_states
from data.languages import languages
from core.functions import get_language, world_debug
from game.entities.ground.ground import Ground
from core.components.skybox import SkyBox
from game.entities.player.player import Player
from panda3d.core import *

class GamePlay(Scene):
    def __init__(self):
        super().__init__()
        self.scene_name = 'game_play'
        
    def config(self):
        # base.cam.setPos(0, -31, 20)
        # base.cam.setHpr(0, -31, 0)
        
        ambientLight = render.attachNewNode(AmbientLight('ambientLight'))
        ambientLight.node().setColor((0.1, 0.1, 0.1, 1))
        render.setLight(ambientLight)
        
        # Create Ambient Light
        my_light = render.attach_new_node(Spotlight("Spot"))
        my_light.node().set_shadow_caster(True, 512, 512)
        my_light.node().set_color((0.9, 0.9, 0.8, 1.0))
        my_light.node().get_lens().set_fov(40)
        my_light.node().get_lens().set_near_far(0.1, 30)
        render.setLight(my_light)
        my_light.set_pos(10, 0, 10)
        my_light.look_at(0, 0, 0)
        # world_debug()
        
    def create(self):
        super().create()
        self.config()
        self.objects['sky'] = SkyBox()
        self.objects['ground'] = Ground()
        self.objects['player'] = Player()
        render.setShaderAuto()

    def update(self, dt):
        self.objects['player'].update(dt)