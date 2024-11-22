# PandaForge

Project template configured for game development using Python with Panda3D

### Scenes

Default scene

```python
from core.scene import Scene
from states.game import game_states

from direct.gui.DirectGui import DirectButton
from direct.gui.OnscreenText import OnscreenText

class MyScene(Scene):
    def __init__(self):
        super().__init__()
        self.scene_name = 'my_scene'
        
    def create(self):
        super().create()
        self.objects['title'] = OnscreenText(
            text="Hello, world!",
            scale=0.1,
            pos=(0, 0.3)
        )
        self.objects['exit_button'] = DirectButton(
            text="Exit",
            scale=0.1,
            pos=(0, 0, -0.1),
            command=exit
        )

    def update(self, dt):
        pass
```

#### Create all objects into (self.objects) in the create method.

Import your scene in the (scenes/__init__.py) directory

__init__.py
```python
from scenes.main_menu import MainMenu
from scenes.settings_menu import SettingsMenu
from scenes.my_scene import MyScene

scenes = {
    "main_menu": MainMenu(),
    "settings_menu": SettingsMenu(),
    "my_scene": MyScene()
}
```

### Change scene

```python
base.change_scene('my_scene')
```

Add overlay scene

```python
from scenes import scenes

my_scene = scenes['my_scene']

# Add overlay scene
my_scene.load()

# Remove overlay scene
my_scene.destroy()
```