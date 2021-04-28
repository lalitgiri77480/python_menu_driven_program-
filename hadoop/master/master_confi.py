import os
import pyttsx3 as p
from hadoop.installation import install_packages

def master():
  os.system("cls")
  p.speak("Enter Your IP Address given below format")
  ip = input("Enter Your Ip Address Eg.(user_name@Ip_Address: ")
      
  while True: 
    f=open("hadoop_master_service.txt","r")
    a="".join(f.readlines())
    print("\u001b[33m"+a)
    print("""
    \u001b[32m 
    Press 1: Install JDK & Hadoop Packages
    Press 2: Configure Master
    Press 3: Format Master Directory
    Press 4: Start Master Services 
    Press 5 :See the Status of Master 
    Press 6: See Report List
    Press 7: BacK TO Menu
    """)
  
  
    p.speak("enter your choice")
    choice = input(" Enter Your Choice : ")
    print("\u001b[33m" +choice)
    
    if int(choice) == 1:
      install_packages.package()
      p.speak("Master Packages Installed")
   
    elif int(choice) == 2:
      
      
      os.system("ssh {0} mkdir /nn ".format(ip))
      os.system("ssh {0} git clone https://github.com/lalitgiri77480/hadoop_confi_file.git ".format(ip))
      os.system("ssh {0} python3 /root/hadoop_confi_file/update_hdfs-site.py ".format(ip))
      os.system("ssh {0} python3 /root/hadoop_confi_file/update_core-site.py ".format(ip))
      p.speak("Master Configured...")
    elif int(choice) == 3:
      
      os.system("ssh {0} hadoop namenode -format ".format(ip))
      p.speak("Master Drive Formated...")
    elif int(choice) == 4:
     
      os.system("ssh {0} hadoop-daemon.sh start namenode ".format(ip))
      p.speak("Namenode service is start ..")
    elif int(choice) == 5:
      p.speak("See the status of Master ")
      os.system("ssh {0} jps ".format(ip))
      
    elif int(choice) == 6:
      
      os.system("ssh {0} hadoop dfsadmin -report ".format(ip))
      p.speak("this is the report of hadoop cluster")
    elif int(choice) == 7:
      break
    else:
      p.speak("Please choose right option")
   

   