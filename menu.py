import os
import getpass
import pyttsx3 as p
from Docker import docker
from hadoop import hadoop_main
os.system("cls")
COLORS = {\
"black":"\u001b[30m",
"red": "\u001b[31m",
"green": "\u001b[32m",
"yellow": "\u001b[33m",
"blue": "\u001b[34m",
"magenta": "\u001b[35m",
"cyan": "\u001b[36m",
"white": "\u001b[37m",
}

def colorText(text):
	for color in COLORS:
	    text=text.replace("[[" + color + "]]" ,COLORS[color])
	return text
engine = p.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 180)     # setting up new voice rate
#"""VOLUME"""
#volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
#engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
f=open("welcomelogo.txt","r")
a="".join(f.readlines())

print(colorText(a))
print()

p.speak("welcome to my menu program !!!")

p.speak("enter your password")
passwd = getpass.getpass("Enter your Password : ")

if passwd != "py":
  p.speak("password incorrect ...")

print()

p.speak("enter yes to continue")
r = input("\u001b[32mEnter yes to Continue : ")
print(r)

def main():

    while True:
        os.system("cls")
        f=open("menu.txt","r")
        a="".join(f.readlines())
        print("\u001b[33m" +a)
        print("""
        \u001b[32m
        Press 1 : About Docker.
        Press 2 : About Hadoop
        Press 3 : About AWS Cloud 
        Press 4 : Ansible Configure
        Press 5 : Web Server Configure
        Press 6 : Machine Learning 
        Press 7 : Exit """)
        p.speak("Enter your Choice")
        choice = input(" Enter Your Choice : \u001b[31m ")
        print(choice)
        if int(choice) == 1:
           docker.docker()
        elif int(choice) == 2:
           hadoop_main.hadoop()
        elif int(choice) == 7:
           os.system("cls")
           f=open("by.txt","r")
           a="".join(f.readlines())
           print("\u001b[32m"+ a)
           p.speak("see you soon , have a nice day")
           exit()
        else:
           input("Invalid Value, Press Enter to Continue")
           continue

        continue


main()


  

     