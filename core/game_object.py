from panda3d.bullet import BulletBoxShape, BulletRigidBodyNode
from panda3d.core import Vec3

class GameObject:
    def __init__(self):
        self.physics_node = None
        self.shape = None
        self.body = None
        self.object = None
        
    def add_rigid_body(self, name, shape=(1, 1, 0.5), mass=1):
        self.shape = BulletBoxShape(shape)
        self.physics_node = BulletRigidBodyNode(f"{name}_physics")
        self.physics_node.addShape(self.shape)
        self.physics_node.setMass(mass)
        self.body = render.attachNewNode(self.physics_node)
        self.body.setPos(self.object.getPos())
        self.object.reparentTo(self.body)
        base.world.attachRigidBody(self.physics_node)
        return self.body

    def remove_from_physics_world(self):
        if self.physics_node:
            base.world.removeRigidBody(self.physics_node)