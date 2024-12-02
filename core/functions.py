import json
from panda3d.core import Vec3
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
    
def get_language():
    preferences = None
    with open('data/json/preferences.json', 'r', encoding='utf-8') as file:
        preferences = json.load(file)
    if preferences['language']['user'] == "":
        return preferences['language']['default']
    else:
        return preferences['language']['user']
    
def ray(start=Vec3(0, 5, 0), end=Vec3(0, -5, 0)):
    start_point = start
    end_point = end 
    result = base.world.rayTestClosest(start_point, end_point)

    if result.hasHit():
        print(f"Objeto atingido: {result.getNode()}")
        print(f"Posição do impacto: {result.getHitPos()}")
        print(f"Normal da colisão: {result.getHitNormal()}")
        
    return result