from states.keys import keys
from core.functions import key
from panda3d.bullet import BulletCharacterControllerNode, BulletCapsuleShape, ZUp
from panda3d.core import Vec3
from direct.actor.Actor import Actor
from core.components.camera_follow import camera_follow

class Player:
    def __init__(self):
        self.height = 1.6
        self.radius = 0.2
        self.speed = 3.0
        self.run_speed = 6.0
        self.rotate_speed = 120.0
        self.is_running = False
        
        self.actor = Actor("assets/models/player/character/act_p3d_chan", {
            'idle': "assets/models/player/character/a_p3d_chan_idle",
            'run': "assets/models/player/character/a_p3d_chan_run"
        })
        self.actor.getChild(0).setZ(-0.75)
        self.actor.getChild(0).setH(180)
        self.animator = self.actor.getAnimControl
        
        self.shape = BulletCapsuleShape(self.radius, self.height - 2*self.radius, ZUp)        
        self.character = BulletCharacterControllerNode(self.shape, 0.4, 'Player')
        
        self.player = render.attachNewNode(self.character)
        
        self.actor.reparentTo(self.player)
        base.world.attachCharacter(self.player.node())
        
        self.player.reparentTo(render)
        
        self.actor.loop('idle')
        
        base.disableMouse()
        base.cam.setPos(0, -3, 3)
        base.cam.setHpr(0, -25, 0)
        base.camLens.setFov(90)

    def movement(self, dt):
        speed = Vec3(0, 0, 0)
        rotate_speed = 0.0
        current_speed = self.speed
        self.is_running = False
        
        if key('lshift'):
            current_speed = self.run_speed
        if key('a'):
            rotate_speed = self.rotate_speed
        if key('d'):
            rotate_speed = -self.rotate_speed
        if key('w'):
            speed.setY(current_speed)
            self.is_running = True
        if key('s'):
            speed.setY(-current_speed)
            self.is_running = True
        
        self.character.setLinearMovement(speed, True)
        self.character.setAngularMovement(rotate_speed)
        self.animate()
        
    def animate(self):
        if self.is_running:
            if not self.animator('run').isPlaying():
                self.actor.stop()
                self.actor.loop('run')
        else:
            if not self.animator('idle').isPlaying():
                self.actor.stop()
                self.actor.loop('idle')

    def update(self, dt):
        self.movement(dt)
        camera_follow(self.player)
        pass
    
    def destroy(self):
        self.actor.removeNode()
        base.world.removeCharacter(self.player.node())