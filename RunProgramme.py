import os

os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/SendToHome.py")

os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/PrimingforPick.py")

#In this programme, you can put particular values onto a text file and the arm will go to that position in the next python file, or even running yolo.py
os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/GetCoordinates.py")  #Gets coordinates and sends to required position
#After it goes to said position, it then performs a pickplace task
os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/UnGrasp.py")

os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/goDown.py")

os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/Grasp.py")

os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/goUp.py")

os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/sendtoTL.py")

os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/goDown.py")

os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/UnGrasp.py")

os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/goUp.py")

os.system("python3 /home/pc/Downloads/PythonRunRos/2_PerceptionBasedPickPlace/SendToHome.py")