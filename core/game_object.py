from panda3d.bullet import BulletBoxShape, BulletRigidBodyNode, BulletTriangleMesh, BulletTriangleMeshShape
from panda3d.core import Vec3

class GameObject:
    def __init__(self):
        self.physics_node = None
        self.shape = None
        self.body = None
        self.object = None
        
    def add_rigid_body(self, name, shape=(1, 1, 0.5), mass=1, pos=None):
        position = None
        if pos:
            position = pos
        else:
            position = self.object.getPos()
        
        self.shape = BulletBoxShape(shape)
        self.physics_node = BulletRigidBodyNode(f"{name}_physics")
        self.physics_node.addShape(self.shape)
        self.physics_node.setMass(mass)
        self.body = render.attachNewNode(self.physics_node)
        self.body.setPos(position)
        self.object.reparentTo(self.body)
        base.world.attachRigidBody(self.physics_node)
        return self.body
    
    def add_collider(self, mass=0):
        nodes = self.object.find_all_matches("**/+GeomNode")        
        for target in nodes:
            mesh = BulletTriangleMesh()
            mesh.add_geom(target.node().get_geom(0))
            shape = BulletTriangleMeshShape(mesh, dynamic=False)
            node = BulletRigidBodyNode(f"{target.name}_physics")
            node.add_shape(shape)
            node.set_mass(mass)
            node_path = render.attach_new_node(node)
            node_path.set_pos(target.getPos())
            node_path.set_hpr(target.getHpr())            
            base.world.attach(node)

    def remove_from_physics_world(self):
        if self.physics_node:
            base.world.removeRigidBody(self.physics_node)