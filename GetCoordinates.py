import os
import time

file=open('/home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/coordinates.txt','r')

content = file.read()
a = content.split()
x=float(a[0])
y=float(a[1])
z=float(a[2])
coord_1=x
coord_2=y
coord_3=z
file.close()

os.system("rosrun kinova_demo pose_action_client.py -v -r j2s7s300 mdeg -- %f %f 0 0 0 0"%(coord_1/1000,coord_2/1000))