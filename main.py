from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import loadPrcFile
from panda3d.bullet import BulletWorld
from states.keys import keys
from states.game import game_states
from config.inputs import accept_inputs, update_keys
loadPrcFile('config/config.prc')
from core.functions import world_debug

from scenes.main_menu import MainMenu
from scenes.settings_menu import SettingsMenu

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        
        self.dt = None        
        self.world = BulletWorld()
        self.world.setGravity(game_states['gravity'])
        world_debug()

        accept_inputs(self)
        self.taskMgr.add(self.update, "update")
        
        self.current_scene = MainMenu()
        
    def update(self, task):
        self.dt = globalClock.getDt()
        self.world.doPhysics(self.dt)
        update_keys()
        self.current_scene.update(self.dt)
        return Task.cont        

game = Game()
game.run()
