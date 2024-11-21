from states.keys import keys
from core.functions import key, handle_input

def accept_inputs(self):
    self.accept("escape", handle_input, ["esc", True])
    self.accept("escape-up", handle_input, ["esc", False])
    self.accept("space", handle_input, ["jump", True])
    self.accept("space-up", handle_input, ["jump", False])

def update_keys():
    if key('w'):
        keys['forward'] = True
    else:
        keys['forward'] = False
    if key('a'):
        keys['left'] = True
    else:
        keys['left'] = False
    if key('s'):
        keys['backward'] = True
    else:
        keys['backward'] = False
    if key('d'):
        keys['right'] = True
    else:
        keys['right'] = False
    if key('lshift'):
        keys['run'] = True
    else:
        keys['run'] = False