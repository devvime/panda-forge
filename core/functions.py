from panda3d.bullet import BulletDebugNode
from states.keys import keys

def handle_input(key, value):
    keys[key] = value
    
def key(key):
    map = base.win.get_keyboard_map()
    button = map.get_mapped_button(key)
    is_down = base.mouseWatcherNode.is_button_down
    return is_down(button)

def world_debug():
    debug_node = BulletDebugNode('Debug')
    debug_node.showWireframe(True)
    debug_node.showConstraints(True)
    debug_node.showBoundingBoxes(False)
    debug_node.showNormals(False)
    debug_np = render.attachNewNode(debug_node)
    base.world.setDebugNode(debug_np.node())
    debug_np.show()