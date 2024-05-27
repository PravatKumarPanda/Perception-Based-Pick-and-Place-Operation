import os
file = open("/home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/coordinates.txt",'r')
content = file.read()
a = content.split()

z=132
z=z*2

coord_3=(0.46-z/1000)

if(coord_3<0.37):
    os.system("rosrun kinova_demo pose_action_client.py -v -r j2s7s300 mdeg -- 0 0 %f 0 0 0"%(coord_3))
else:
    os.system("rosrun kinova_demo pose_action_client.py -v -r j2s7s300 mdeg -- 0 0 0.37 0 0 0")
