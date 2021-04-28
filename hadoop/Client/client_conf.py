import os
import pyttsx3 as p
from hadoop.installation import install_packages

def slave():
  p.speak("Enter Your IP Address")
  ip = input("Enter Your Ip Address Eg.(user_name@Ip_Address: ")
  
  while True: 
    print(""" 
    Press 1: Install JDK & Hadoop Packages 
    Press 2: Configure the Client
    Press 3: Start Slave Services
    Press 4: See the status of Client 
    Press 5: Create Directory
    Press 6: Create file
    Press 7: Upload file
    Press 8: View Or Read File
    Press 9: Change Directory
    Press 10: BacK TO Menu
    """)
  
  
    p.speak("enter your choice")
    choice = input(" Enter Your Choice : ")
    print("\u001b[33m" +choice)
    
    if int(choice) == 1:
      install_packages.packages()
      p.speak("Client Packages Installed")
   
    elif int(choice) == 2:
      
      os.system("ssh {0} git clone https://github.com/lalitgiri77480/slave_confi_file.git ".format(ip))
      os.system("ssh {0} python3 /root/slave_confi_file/update_core-site.py ".format(ip))
      p.speak("Client Configured...")

    elif int(choice) == 3:
      os.system("ssh {0} hadoop-daemon.sh start datanode ".format(ip))
      p.speak("Datanode Service Start..")
    elif int(choice) == 4:
      os.system("ssh {0} jps ".format(ip))
      p.speak("See the status of Client...")
    elif int(choice) == 5:
      p.speak("Enter your directory name ")
      dir= input("Enter Your Directory Name")
      os.system("ssh {0} mkdir {1} ".format(ip,dir))
      p.speak("Directory is created... ")
    elif int(choice) == 6:
      p.speak("Enter your file with extension that you want name ")
      file= input("Enter Your File Name With Extension:")
      os.system("ssh {0} {1} ".format(ip,file))
      p.speak("File is created... ")
    elif int(choice) == 7:
      p.speak("Enter your file with extension that you want name ")
      file= input("Enter Your File Name With Extension:")
      os.system("ssh {0} hadoop fs -put {1} ".format(ip,file))
      p.speak("File is uploaded...")
    elif int(choice) == 8:
      p.speak("Enter your file with extension that you want name ")
      file= input("Enter Your File Name With Extension:")
      os.system("ssh {0} hadoop fs -cat {1} ".format(ip,file))
    elif int(choice) == 9:
      p.speak("Enter your directory path ")
      file= input("Enter your directory path:")
      os.system("ssh {0} cd {1} ".format(ip,file))
      
    elif int(choice) == 10:
      break
    else:
      p.speak("Please choose right option")
   

   