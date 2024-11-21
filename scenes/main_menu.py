from panda3d.core import NodePath, PandaNode, TextNode
from direct.gui.DirectGui import DirectButton, DirectLabel
from direct.gui.OnscreenText import OnscreenText
from states.game import game_states

class MainMenu:
    def __init__(self):
        self.scene_name = 'main_menu'
        self.is_loaded = False
        self.objects = {}
        
    def create(self):
        self.objects['title'] = OnscreenText(
            text="Main Menu",
            scale=0.1,
            pos=(0, 0.3)
        )
        self.objects['start_button'] = DirectButton(
            text="Start Game",
            scale=0.1,
            pos=(0, 0, 0.1),
            command=go_to_settings_menu
        )
        self.objects['exit_button'] = DirectButton(
            text="Exit",
            scale=0.1,
            pos=(0, 0, -0.1),
            command=exit
        )
        
    def load(self):
        self.scene = NodePath(self.scene_name)
        self.scene.reparentTo(render)
        self.create()
        self.is_loaded = True
    
    def update(self, dt):
        pass
    
    def destroy(self):
        self.scene.removeNode()
            
def go_to_settings_menu():
    base.change_scene('settings_menu')