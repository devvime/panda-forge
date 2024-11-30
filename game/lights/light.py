from panda3d.core import *

def ambient_light(color=(0.2, 0.2, 0.2, 1)):
    a_light = render.attachNewNode(AmbientLight('a_light'))
    a_light.node().setColor(color)
    render.setLight(a_light)
    return a_light
    
def directional_light(color=(0.9, 0.9, 0.8, 1.0), pos=(10, -10, 15), hpr=(0, 0, 0)):
    d_light = render.attach_new_node(DirectionalLight("d_light"))
    d_light.node().set_shadow_caster(True, 1024, 1024)
    d_light.node().set_color(color)
    d_light.node().get_lens().set_fov(100)
    d_light.node().get_lens().set_film_size(20, 20)
    d_light.node().get_lens().set_near_far(10, 100)
    d_light.set_pos(pos)
    d_light.set_hpr(hpr)
    d_light.look_at(0, 0, 0)
    render.setLight(d_light)
    return d_light