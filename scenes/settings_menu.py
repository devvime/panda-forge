from panda3d.core import NodePath, PandaNode, TextNode
from direct.gui.DirectGui import DirectButton, DirectLabel
from direct.gui.OnscreenText import OnscreenText
from states.game import game_states

class SettingsMenu:
    def __init__(self):
        self.is_loaded = False
        self.scene = NodePath("settings_menu")
        self.objects = {}
        self.create()
        self.load_scene()
        
    def create(self):
        self.objects['title'] = OnscreenText(
            text="Settings Menu",
            scale=0.1,
            pos=(0, 0.3)
        )
        self.objects['main_menu_button'] = DirectButton(
            text="Back to Main Menu",
            scale=0.1,
            pos=(0, 0, 0.1),
            command=None
        )
        self.objects['exit_button'] = DirectButton(
            text="Exit",
            scale=0.1,
            pos=(0, 0, -0.1),
            command=exit
        )
        
    def load_scene(self):
        for obj in self.objects.items():
            if isinstance(obj, NodePath) or isinstance(obj, PandaNode) or isinstance(obj, (DirectButton, DirectLabel, TextNode)):
                element.reparentTo(self.scene)
        self.scene.reparentTo(render)
        self.is_loaded = True
    
    def update(self, dt):
        pass
    
    def destroy(self):
        self.scene.removeNode()