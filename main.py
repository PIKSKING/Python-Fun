import os
import funcs
import random 
import time
from threading import Thread


def mainfunc():
    os.system("cls")

    print(""" 




                ~~~WELCOME TO PIKS ADVENTURE GAME~~~ """)


    while True:
        print("""



                1. New Adventure
                2. Credits
                3. Options
                4. Exit


        """)

        piks = int(input("please pick an option: "))


        if piks == 4:
            quit()

        elif piks == 2:
            os.system("cls")
            funcs.five_dots()
            print("This Game Project Was Made by Pouria Aghaei Shahvali")
            funcs.five_dots()
            time.sleep(3)
            os.system("cls")

        elif piks == 3:
            print(""" 
                    1-change color 
                    2-play song
            """)
            option = int(input("please enter an option: "))
            if option == 1:
                funcs.color_change()
            elif option == 2:
                if __name__ == '__main__':
                    Thread(target = funcs.playsong).start()
                    Thread(target = mainfunc).start()    

            
        elif piks ==1:
            os.system("cls")
            print("""YOU WAKE UP ON A BEACH...
            
                1-MOVE TO THE JUNGLE
                2-STAY IN THE BEACH AND LOOK FOR PEOPLE

            """)
            decision = int(input("~"))
            if decision == 1:
                os.system("cls")
                funcs.jungle()
                quit()
            elif decision == 2:
                os.system("cls")
                funcs.beach()
                quit()
            







mainfunc()