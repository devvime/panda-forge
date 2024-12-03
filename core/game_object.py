from panda3d.bullet import BulletBoxShape, BulletRigidBodyNode, BulletTriangleMesh, BulletTriangleMeshShape, BulletSphereShape
from panda3d.core import Vec3

class GameObject:
    def __init__(self):
        self.node = None
        self.shape = None
        self.body = None
        self.object = None
        
    def add_rigid_body(self, name, shape=(1, 1, 1), mass=1, pos=None, type='box', radius=1):
        position = None
        if pos:
            position = pos
        else:
            position = self.object.getPos()
        
        if type == 'box':    
            self.shape = BulletBoxShape(shape)
        elif type == 'sphere':
            self.shape = BulletSphereShape(radius)
        
        self.node = BulletRigidBodyNode(f"{name}_physics")
        self.node.addShape(self.shape)
        self.node.setMass(mass)
        self.body = render.attachNewNode(self.node)
        self.body.setPos(position)
        self.object.reparentTo(self.body)
        base.world.attachRigidBody(self.node)
        return self.body
    
    def add_mesh_collider(self, mass=0):
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
        if self.node:
            base.world.removeRigidBody(self.node)
            
    def on_collisiton(self, input, other_name):
        contact_result = base.world.contactTest(input.node())

        if contact_result.getNumContacts() > 0:
            for contact in contact_result.getContacts():
                if contact.getNode1().name == other_name:
                    return {
                        "collision": True,
                        "name": contact.getNode1().name,
                        "position": contact.getManifoldPoint().getPositionWorldOnA()
                    }
                else:
                    return {
                        "collision": False,
                        "name": None,
                        "position": None
                    }