from panda3d.core import NodePath

class Scene:
    def __init__(self):
        self.scene_name = None
        self.is_loaded = False
        self.objects = {}
        
    def create(self):
        pass
        
    def load(self):
        self.scene = NodePath(self.scene_name)
        self.scene.reparentTo(render)
        self.create()
        self.is_loaded = True
        
    def destroy(self):
        for obj in self.objects:
            self.objects[obj].destroy()
        self.scene.removeNode()