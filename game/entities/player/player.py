from states.keys import keys
from core.functions import key
from panda3d.bullet import BulletCharacterControllerNode, BulletCapsuleShape, ZUp
from panda3d.core import Vec3
from direct.actor.Actor import Actor
from core.components.camera_follow import camera_follow

class Player:
    def __init__(self):
        self.height = 2
        self.radius = 0.2
        self.gravity = 25.0
        self.speed = 3.0
        self.run_speed = 8.0
        self.rotate_speed = 160.0
        self.max_jump_height = 5.0
        self.jump_speed = 8
        self.is_walking = False
        self.is_running = False
        self.is_jumping = False
        
        self.actor = Actor("assets/models/player/player1.gltf")
        self.actor.getChild(0).setZ(-0.99)
        self.actor.getChild(0).setH(180)
        self.animator = self.actor.getAnimControl
        
        self.shape = BulletCapsuleShape(self.radius, self.height - 2*self.radius, ZUp)        
        self.character = BulletCharacterControllerNode(self.shape, 0.8, 'Player')
        self.character.set_gravity(self.gravity)
        
        self.player = render.attachNewNode(self.character)
        self.player.set_pos(0, 0, .5)
        
        self.actor.reparentTo(self.player)
        base.world.attachCharacter(self.player.node())
        
        self.player.reparentTo(render)
        
        self.actor.loop('idle')
        
        base.disableMouse()
        base.cam.setPos(0, -3, 2.5)
        base.cam.setHpr(0, -20, 0)
        base.camLens.setFov(90)

    def movement(self, dt):
        speed = Vec3(0, 0, 0)
        rotate_speed = 0.0
        current_speed = self.speed
        self.is_walking = False
        self.is_running = False
        
        if self.character.on_ground:
            self.is_jumping = False
        else:
            self.is_jumping = True
        
        if key('space'):
            self.doJump()
            
        if key('lshift'):
            self.is_running = True
            
        if key('a'):
            rotate_speed = self.rotate_speed
        if key('d'):
            rotate_speed = -self.rotate_speed
                
        if key('w'):
            self.is_walking = True                
            speed.setY(current_speed)
            
        if key('s'):
            self.is_walking = True    
            speed.setY(-current_speed)            
            
        if self.is_walking and self.is_running:
            current_speed = self.run_speed                
            speed.setY(current_speed)
        
        self.character.setLinearMovement(speed, True)
        self.character.setAngularMovement(rotate_speed)
        self.animate()
        
    def animate(self):
        if self.is_walking and not self.is_running and not self.is_jumping:
            if not self.animator('walk').isPlaying():
                self.actor.stop()
                self.actor.loop('walk')
        elif self.is_walking and self.is_running and not self.is_jumping:
            if not self.animator('run').isPlaying():
                self.actor.stop()
                self.actor.loop('run')
        elif self.is_jumping:
            if not self.animator('fall').isPlaying():
                self.actor.stop()
                self.actor.loop('fall')
        else:
            if not self.animator('idle').isPlaying():
                self.actor.stop()
                self.actor.loop('idle')
    
    def doJump(self):
        self.character.setMaxJumpHeight(self.max_jump_height)
        self.character.setJumpSpeed(self.jump_speed)
        self.character.doJump()

    def update(self, dt):
        self.movement(dt)
        camera_follow(target=self.player)
        pass
    
    def destroy(self):
        self.actor.removeNode()
        base.world.removeCharacter(self.player.node())
