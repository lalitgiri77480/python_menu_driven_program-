import os
import pyttsx3 as p
from hadoop.master import master_confi
from hadoop.Slave import slave_conf
def hadoop():
    os.system("cls")
    while True :
        f=open("hadoop.txt","r")
        a="".join(f.readlines())
        print("\u001b[33m"+a)
        print("""
        \u001b[32m
        Press 1: Hadoop Master  
        Press 2: Hadoop Slave
        Press 3: Hadoop Client
        Press 4: View Hadoop Web UI 
        Press 5: Return to Main Menu
        Press 6: Exit
        """)

        # user input entered
        p.speak("Enter your Choice...")
        var = int(input("Enter the option: "))
        if var == 1:
            master_confi.master()

        elif var == 2:
            slave_conf.slave()
        elif var == 3:
            client_confi.client()
        elif var == 5:
            break
        elif var == 6:
            exit()

        else:
            input("Invalid Value, Press Enter to Continue")
            p.speak("please choose right option")
            continue
