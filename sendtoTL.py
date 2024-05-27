
import os
file=open("/home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/coordinates.txt",'r')

content1 = file.read()

a = content1.split()
pickupx=float(a[0])
pickupy=float(a[1])
pickupz=float(a[2])
file.close()
pickupy=-pickupy/1000
pickupx=-pickupx/1000

if(pickupy>-300 or (pickupy<-300 and pickupx>0)):
    #Send to homeprime position:
    os.system("rosrun kinova_demo pose_action_client.py -v -r j2s7s300 mdeg -- %f %f 0 0 0 0"%(pickupx,pickupy))

    file=open("/home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/targetloc.txt",'r')

    content2=file.read()

    b = content2.split()


    targetx=float(b[0])
    targety=float(b[1])
    targetz=float(b[2])
    file.close()
    cordx=targetx/1000
    cordy=targety/1000
    cordz=targetz/1000

    os.system("rosrun kinova_demo pose_action_client.py -v -r j2s7s300 mdeg -- %f 0 0 0 0 0"%(cordx))
    os.system("rosrun kinova_demo pose_action_client.py -v -r j2s7s300 mdeg -- 0 %f 0 0 0 0"%(cordy))
else:
    file=open("/home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/targetloc.txt",'r')

    content2=file.read()

    b = content2.split()


    targetx=float(b[0])
    targety=float(b[1])
    targetz=float(b[2])

    cordx=targetx-pickupx
    cordy=targety-pickupy
    cordz=targetz-pickupz
    cordx=cordx/1000
    cordy=cordy/1000
    cordz=cordz/1000
    file.close()
    os.system("rosrun kinova_demo pose_action_client.py -v -r j2s7s300 mdeg -- %f %f 0 0 0 0"%(cordx,cordy))
    