import os
import pyttsx3 as p
from hadoop.installation import install_packages

def slave():
  p.speak("Enter Your IP Address")
  ip = input("Enter Your Ip Address Eg.(user_name@Ip_Address: ")
  
  while True: 
    print(""" 
    Press 1: Install JDK & Hadoop Packages
    Press 2: Configure Slave
    Press 3: Start Slave Services
    Press 4: See the status of Slave  
    Press 5: BacK TO Menu
    """)
  
  
    p.speak("enter your choice")
    choice = input(" Enter Your Choice : ")
    print("\u001b[33m" +choice)
    
    if int(choice) == 1:
      install_packages.packages()
      p.speak("Slave Packages Installed")
   
    elif int(choice) == 2:
      
      os.system("ssh {0} mkdir /nn ".format(ip))
      os.system("ssh {0} git clone https://github.com/lalitgiri77480/slave_confi_file.git ".format(ip))
      os.system("ssh {0} python3 /root/slave_confi_file/update_hdfs-site.py ".format(ip))
      os.system("ssh {0} python3 /root/slave_confi_file/update_core-site.py ".format(ip))
      p.speak("Master Configured...")

    elif int(choice) == 3:
      os.system("ssh {0} hadoop-daemon.sh start datanode ".format(ip))
      p.speak("Datanode Service Start..")
    elif int(choice) == 4:
      os.system("ssh {0} jps ".format(ip))
      p.speak("See the status of Slave ")
    elif int(choice) == 5:
      break
    else:
      p.speak("Please choose right option")
   

   