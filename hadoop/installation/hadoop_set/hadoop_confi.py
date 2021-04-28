import os
import pyttsx3 as p

def hadoop():
    login=input("Enter your IP Address Eg. (User@IP Address)")
    p.speak("Enter your IP Address")
    print(" Packages Download in process.....")
    os.system("ssh {0} yum install git -y ".format(login))
    os.system("ssh {0} git clone https------".format(login))
    print(" Hadoop packages download , installing process start.....")
    p.speak("hadoop packages download , installing process start")
    os.system("ssh {0} rpm -ivh hadoop-1.2.1-1.x86_64.rpm".format(login))
    print(" Hadoop Packages Installed :)")
    p.speak("Hadoop Packages Installed ")
    os.system("ssh {login} hadoop version")
    p.speak(" This is Hadoop Packages Installed ")
    