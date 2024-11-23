from core.game_object import GameObject

class Ground(GameObject):
    def __init__(self):
        super().__init__()
        self.object = loader.loadModel("assets/models/scene/ground/ground")
        self.object.reparentTo(render)        
        self.add_rigid_body('ground', shape=(10, 10, 0.3), mass=0)

    def update(self, dt):
        pass
