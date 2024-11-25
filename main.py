from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import *
from panda3d.bullet import BulletWorld
loadPrcFile('config/config.prc')

from states.keys import keys
from states.game import game_states
from config.inputs import accept_inputs, update_keys
from scenes import scenes

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        
        self.win.setClearColor(LVector4(0.53, 0.81, 0.92, 1))
        
        self.dt = None        
        self.world = BulletWorld()
        self.world.setGravity(game_states['gravity'])

        accept_inputs(self)
        self.taskMgr.add(self.update, "update")
        
        self.current_scene = None
        self.scenes = scenes        
        self.change_scene('game_play')
        
    def update(self, task):
        if game_states['paused']: return
        self.dt = globalClock.getDt()
        self.world.doPhysics(self.dt)
        update_keys()
        self.update_current_scene()
        return Task.cont
    
    def change_scene(self, scene):
        if self.current_scene:
            for obj in self.current_scene.objects:
                self.current_scene.objects[obj].destroy()                
            self.current_scene.destroy()
        self.current_scene = self.scenes[scene]
        self.current_scene.load()
    
    def update_current_scene(self):
        if self.current_scene and self.current_scene.is_loaded:
            self.current_scene.update(self.dt)

game = Game()
game.run()
