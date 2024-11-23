from core.scene import Scene
from states.game import game_states
from data.languages import languages
from core.functions import get_language, world_debug
from game.entities.ground.ground import Ground
from panda3d.core import AmbientLight, DirectionalLight, Vec4
from core.components.skybox import SkyBox
from game.entities.player.player import Player

class GamePlay(Scene):
    def __init__(self):
        super().__init__()
        self.scene_name = 'game_play'
        
    def config(self):
        # base.cam.setPos(0, -31, 20)
        # base.cam.setHpr(0, -31, 0)
        
        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        self.ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(self.ambientLightNodePath)
        
        mainLight = DirectionalLight("main light")
        mainLight.setShadowCaster(True, 512, 512)
        self.mainLightNodePath = render.attachNewNode(mainLight)
        self.mainLightNodePath.setHpr(45, -45, 0)
        render.setLight(self.mainLightNodePath)
        
        render.setShaderAuto()
        # world_debug()
        
    def create(self):
        super().create()
        self.config()
        self.sky = SkyBox()
        self.ground = Ground()
        self.player = Player()
        render.setShaderAuto()

    def update(self, dt):
        self.player.update(dt)