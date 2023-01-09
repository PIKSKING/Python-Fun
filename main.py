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

        kaiser = int(input("please pick an option: "))


        if kaiser == 4:
            quit()

        elif kaiser == 2:
            os.system("cls")
            funcs.five_dots()
            print("this project was made by piks")
            funcs.five_dots()
            time.sleep(3)

        elif kaiser == 3:
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

            
        elif kaiser ==1:
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