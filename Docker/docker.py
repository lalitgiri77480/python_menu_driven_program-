import os
import pyttsx3 as p
def docker():
  p.speak("Enter Your IP Address ")
  ip = input("\u001b[36m Enter Your IP Address {eg. root@192.168.43.152} ")
  print("\u001b[36m Your IP Address:"+ ip)
  while True:
       os.system("cls")
       f=open("docker_asci.txt","r")
       a="".join(f.readlines())
       print("\u001b[33m" +a)
       print("""
       \n
       \u001b[32m
       Press 1 : Install Docker
       Press 2 : Start  Docker Services
       Press 3 : Image Pull
       Press 4 : See Docker Images
       Press 5 : Create Container
       Press 6 : See list of contrainer running
       Press 7 : exit
       """)
       p.speak("enter your choice")
       choice = input(" Enter Your Choice : ")
       print("\u001b[33m" +choice)

       if int(choice) == 1:
          os.system("ssh {0} yum install docker-ce --nobest -y".format(ip))
          p.speak("docker is now configured in your system")
       elif int(choice) == 2:
          os.system("ssh {0} systemctl start docker".format(ip))
          p.speak("docker service started")
       elif int(choice) == 3:
          imgname = input(" \n Enter image name that you want to PULL...")
          os.system("ssh {0} docker pull centos".format(ip))
          p.speak("cent os image successfully pulled")
       elif int(choice) == 4:
          p.speak("This are Docker Images we have ")
          os.system("ssh {0} docker images".format(ip))   
       elif int(choice) == 5:
          p.speak("Enter container name")
          osname = input("\n \u001b[34mEnter Container Name : ")
          p.speak("Enter container name")
          imgname = input("\n Enter Image Name : ")
          print("\u001b[37m"+ imgname)
          os.system("ssh {0} docker run -dit --name {1} -p 8080:80 {2}".format(ip,osname,imgname))
          p.speak("{0} container launched".format(imgname))
       elif int(choice) == 6:
          p.speak("This Container are running ")
          os.system("ssh {0} docker ps".format(ip))
          
       elif int(choice) == 7:
          break
       elif int(choice) == 8:
          exit()
       else:
          p.speak("Please check   it is  not supported")
    
       input("\n \u001b[34m Press Enter to continue....")
       
