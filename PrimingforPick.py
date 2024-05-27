import os
print("Priming the gripper for picking without rotation as per orientation of object")
joint_1=0
joint_2=0
joint_3=0
joint_4=20
joint_5=95
joint_6=0
joint_7=0

os.system("rosrun kinova_demo joints_action_client.py -v -r j2s7s300 degree -- %d %d %d %d %d %d %d" 
          
          
          %(joint_1,joint_2,joint_3,joint_4,joint_5,joint_6,joint_7))

print("Sent to pickup point")