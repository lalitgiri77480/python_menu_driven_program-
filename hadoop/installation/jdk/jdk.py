import os
import pyttsx3 as p

def jdk():
    login=input("Enter your IP Address Eg. (User@IP Address)")
    p.speak("Enter your IP Address")
    print(" Packages Download in process.....")
    os.system("ssh {0} yum install git -y ".format(login))
    os.system("ssh {0} git clone htttps".format(login))
    print(" jdk packages download , installing process start.....")
    p.speak("jdk packages download , installing process start")
    os.system("ssh {0} rpm -ivh jdk-84171-linux-x64.rpm".format(login))
    print(" JDK Packages Installed :)")
    p.speak("JDK Packages Installed ")
    print(" JDK Package Version.....")
    os.system("ssh {login} java -version")
    p.speak(" This is JDK Packages Installed ")
    

    