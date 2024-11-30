from core.game_object import GameObject

class Ground(GameObject):
    def __init__(self):
        super().__init__()
        self.object = loader.loadModel("assets/models/scene/egg/propotype_env")
        self.object.reparentTo(render)        
        self.add_rigid_body('ground', shape=(20, 20, 0.5), mass=0)

    def update(self, dt):
        pass
