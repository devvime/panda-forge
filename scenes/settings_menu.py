from core.scene import Scene
from states.game import game_states

from direct.gui.DirectGui import DirectButton
from direct.gui.OnscreenText import OnscreenText

class SettingsMenu(Scene):
    def __init__(self):
        super().__init__()
        self.scene_name = 'settings_menu'
        
    def create(self):
        super().create()
        self.objects['title'] = OnscreenText(
            text="Settings Menu",
            scale=0.1,
            pos=(0, 0.3)
        )
        self.objects['main_menu_button'] = DirectButton(
            text="Back to Main Menu",
            scale=0.1,
            pos=(0, 0, 0.1),
            command=go_to_main_menu
        )
        self.objects['exit_button'] = DirectButton(
            text="Exit",
            scale=0.1,
            pos=(0, 0, -0.1),
            command=exit
        )

    def update(self, dt):
        pass

def go_to_main_menu():
    base.change_scene('main_menu')