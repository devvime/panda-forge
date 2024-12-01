def camera_follow(target=None, offset=(0, -0.5, 0.05), smooth=0.08):
    target_position = target.getPos() + offset
    target_rotation = target.getHpr() + offset
    
    current_position = base.camera.getPos()
    current_rotation = base.camera.getPos()
    
    new_position = current_position + (target_position - current_position) * smooth
    new_rotation = current_rotation + (target_rotation - current_rotation) + smooth
    
    base.camera.setPos(new_position)
    base.camera.setHpr(new_rotation)
    # base.camera.lookAt(target)