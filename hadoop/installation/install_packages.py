import os
import pyttsx3 as p
from hadoop.installation.jdk import jdk
from hadoop.installation.hadoop_set import hadoop_confi
def package():
   while True:
     f=open("install_packages.txt","r")
     a="".join(f.readlines())
     print("\u001b[33m"+a)
     print(""" 
     \u001b[32m
     Press 1: Install JDK Packages
     Press 2: Install Hadoop Packages
     Press 3: Check Version JDK Install
     Press 4: Check Version Hadoop Install
     Press 5: Back To Menu
     """)
    
     choice= int(input("Enter your Choice: "))
     p.speak("Enter your Choice")
     if int(choice) == 1:
       jdk.jdk()
     elif int(choice) == 2:
       hadoop_confi.hadoop()
     elif int(choice) == 3:
       ip= input("Enter Your Ip Address: ")
       p.speak("Enter your IP Address")
       os.system("ssh {0} java -version ".format(ip)) 
     elif int(choice) == 4:
       ip= input("Enter Your Ip Address: ")
       p.speak("Enter your IP Address")
       os.system("ssh {0} hadoop version ".format(ip)) 
     elif int(choice) == 5:
       p.speak("Back to menu ...")
       break