import os
import funcs
import random 
import time


os.system("cls")

print(""" 




            ~~~WELCOME TO PIKS MADLIBS GAME~~~ """)


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
        """)
        option = int(input("please enter an option: "))
        if option == 1:
            funcs.color_change()
        
