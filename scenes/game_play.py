from core.scene import Scene
from states.game import game_states
from data.languages import languages
from core.functions import get_language

class GamePlay(Scene):
    def __init__(self):
        super().__init__()
        self.scene_name = 'game_play'
        
    def create(self):
        super().create()

    def update(self, dt):
        pass