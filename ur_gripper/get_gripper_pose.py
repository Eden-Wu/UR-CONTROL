
# 机械臂TCP相对于base的位姿
import  math
import transformations
import numpy as np

# 从urbasic得到的tcp位姿并转化为4*4
x, y, z, rx, ry, rz = 0.5, 0.3, 0.2, math.pi/4, math.pi/6, math.pi/3

pose_matrix = transformations.euler_matrix(rx, ry, rz, 'sxyz')

pose_matrix[:3, 3] = [x, y, z]

print(f'TCP_pose_matrics\n:{pose_matrix}')



# 定义gripper在TCP坐标系的位姿并且转换为4*4
x, y, z, rx, ry, rz = 0, 0, 0.2, 0,0, 0

T_pose_matrix= transformations.euler_matrix(rx, ry, rz, 'sxyz')
T_pose_matrix[:3, 3] = [x, y, z]

print(f'gripper在tcp坐标系下的位姿\n:{T_pose_matrix}')


# 计算物体在世界坐标系的4*4 和 位姿（x,y,z,rx,ry,rz)
gripper_matrics = np.dot(pose_matrix, T_pose_matrix)

x1,y1,z1 = gripper_matrics[:3, 3]
rx1,ry1,rz1 = transformations.euler_from_matrix(gripper_matrics, 'rxyz')

gripper_pose = [x1,y1,z1,rx1,ry1,rz1]

print(f'gripper_matrics：\n{gripper_matrics}')

print(f'gripper_pose：\n{gripper_pose}')


