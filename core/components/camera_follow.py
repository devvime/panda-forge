def camera_follow(target, offset=(0, -1.5, 0.1), smooth=0.01):
    target_position = target.getPos() + offset
    current_position = base.camera.getPos()
    new_position = current_position + (target_position - current_position) * smooth
    base.camera.setPos(new_position)
    base.camera.lookAt(target)