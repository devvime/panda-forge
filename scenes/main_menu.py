from core.scene import Scene
from states.game import game_states
from data.languages import languages
from core.functions import get_language

from direct.gui.DirectGui import DirectButton
from direct.gui.OnscreenText import OnscreenText

class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        self.scene_name = 'main_menu'
        
    def create(self):
        super().create()
        self.objects['title'] = OnscreenText(
            text=languages[get_language()]['main_menu']['title'],
            scale=0.1,
            pos=(0, 0.5)
        )
        self.objects['start_button'] = DirectButton(
            text=languages[get_language()]['main_menu']['start_button'],
            scale=0.1,
            pos=(0, 0, 0.3),
            command=start_game
        )
        self.objects['settings_button'] = DirectButton(
            text=languages[get_language()]['main_menu']['settings_button'],
            scale=0.1,
            pos=(0, 0, 0.1),
            command=go_to_settings_menu
        )
        self.objects['exit_button'] = DirectButton(
            text=languages[get_language()]['main_menu']['exit_button'],
            scale=0.1,
            pos=(0, 0, -0.1),
            command=exit
        )

    def update(self, dt):
        pass

def start_game():
    base.change_scene('game_play')
    
def go_to_settings_menu():
    base.change_scene('settings_menu')