def camera_follow(target, offset=(0, -2, 0.5), smooth=0.05):
    target_position = target.getPos() + offset
    current_position = base.camera.getPos()
    new_position = current_position + (target_position - current_position) * smooth
    base.camera.setPos(new_position)