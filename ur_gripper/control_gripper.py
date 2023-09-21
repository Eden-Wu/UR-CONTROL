from robotiq_gripper import RobotiqGripper

# ip = '127.0.0.1'
ip = '192.168.1.102'
def control_gripper():
    gripper = RobotiqGripper()
    gripper.connect(ip, 63352)  # 请替换为实际的夹爪地址和端口

    # 激活夹爪
    gripper.activate()

    # 关闭夹爪
    position = gripper.get_closed_position()
    speed = 100
    force = 100
    gripper.move_and_wait_for_pos(position, speed, force)

    # 移动夹爪到指定位置
    position = 150  # 请根据实际情况设置位置值
    speed = 100
    force = 100
    gripper.move_and_wait_for_pos(position, speed, force)

    # 获取当前速度、位置和力量
    speed = gripper._get_var(gripper.SPE)
    position = gripper._get_var(gripper.POS)
    force = gripper._get_var(gripper.FOR)

    gripper.disconnect()

    return speed, position, force

# 调用控制函数
gripper_speed, gripper_position, gripper_force = control_gripper()

print("夹爪速度:", gripper_speed)
print("夹爪位置:", gripper_position)
print("夹爪力量:", gripper_force)







