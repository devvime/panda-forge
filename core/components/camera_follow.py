from panda3d.core import Point3

def camera_follow(target=None, offset=(0, -0.5, -0.5), smooth=0.05):
    target_position = target.getPos() + offset
    target_rotation = target.getHpr() + offset
    
    current_position = base.camera.getPos()
    current_rotation = base.camera.getPos()
    
    new_position = current_position + (target_position - current_position) * smooth
    new_rotation = current_rotation + (target_rotation - current_rotation) + smooth
    
    base.camera.setPos(new_position)
    base.camera.setHpr(new_rotation)

class CameraFollow:
    
    def __init__(self, target):
        base.disableMouse()
        self.player = target
        self.camera_distance = 2
        self.camera_angle = [0, 10]
        self.mouse_sensitivity = 0.1
        self.center_mouse()        

    def update(self):
        if base.mouseWatcherNode.hasMouse():
            
            center_x = base.win.getProperties().getXSize() // 2
            center_y = base.win.getProperties().getYSize() // 2
            
            mouse = base.win.getPointer(0)
            x = mouse.getX()
            y = mouse.getY()
            
            delta_x = x - center_x
            delta_y = y - center_y
            
            self.camera_angle[0] -= delta_x * self.mouse_sensitivity
            self.camera_angle[1] += delta_y * self.mouse_sensitivity
            self.camera_angle[1] = max(-35, min(65, self.camera_angle[1]))
            
            self.center_mouse()
        
        x = self.camera_distance * -self.sin(self.camera_angle[0])
        y = self.camera_distance * self.cos(self.camera_angle[0])
        z = self.camera_distance * self.sin(self.camera_angle[1])
        
        base.camera.setPos(self.player.getPos() + Point3(x, y, z))
        base.camera.lookAt(self.player)

    def center_mouse(self):
        center_x = base.win.getProperties().getXSize() // 2
        center_y = base.win.getProperties().getYSize() // 2
        base.win.movePointer(0, center_x, center_y)

    def sin(self, angle):
        from math import sin, radians
        return sin(radians(angle))

    def cos(self, angle):
        from math import cos, radians
        return cos(radians(angle))