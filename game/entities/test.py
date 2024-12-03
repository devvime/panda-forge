from core.game_object import GameObject

class Test(GameObject):
    def __init__(self):
        super().__init__()
        self.object = loader.loadModel("assets/models/cube")
        self.object.reparentTo(render)     
        self.add_rigid_body(name='test', pos=(5, 5, 3))

    def update(self, dt):
        # print(self.on_collisiton(self.body, 'Player'))
        pass


