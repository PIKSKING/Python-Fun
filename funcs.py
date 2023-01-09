import os
import time

def color_change():
    print("""
        0 = Black       8 = Gray
        1 = Blue        9 = Light Blue
        2 = Green       A = Light Green
        3 = Aqua        B = Light Aqua
        4 = Red         C = Light Red
        5 = Purple      D = Light Purple
        6 = Yellow      E = Light Yellow
        7 = White       F = Bright White
    """)
    color = input("please enter a color: ")
    os.system("cls")
    os.system(f"color {color}")
    print("""~~~color changed successfully~~~""")
    five_dots()




def five_dots():
    dot = 0
    while dot<5:
        print(".")
        time.sleep(0.05)
        dot = dot+1






def jungle():
    print("""OH NO! 
        THE JUNGLE IS TOO DARK, YOU CAN'T GO FURTHER
        1-GO BACK TO THE BEACH
        2-MAKE A CAMPFIRE
    """)
    oppp1 = int(input("~"))
    
    if oppp1 == 1:
        os.system("cls")
        print("""OH NO!
                IT'S TOO DARK!!! YOU CAN'T GO FURTHER
                YOU HAVE TO GO BACK TO THE BEACH
            """)
        input("press enter")
        os.system("cls")
        print("""
                ON YOUR WAY TO THE BEACH, A PANTHER BLOCKS YOUR WAY AND ATTACKS YOU...
                SORRY, YOU DIE
            """)

    elif oppp1 == 2:
        os.system("cls")
        print("""WHEN YOU TRY TO GATHER THE WOOD TO MAKE A CAMPFIRE, YOU GET REALLY TIRED BECAUSE IT'S DARK AND IT'S HARD TO FIND WOOD
        YOU HAVE TO SLEEP, YOU CAN'T MAKE THE CAMPFIRE NOW...
        1-SLEEP FOR NOW WITH YOUR CLOTHES
        2-MAKE A TENT AND A SPEAR
        """)
        oppp5 = int(input("~"))
        os.system("cls")
        if oppp5 == 1:
            print("""
                GOOD MORNING!!!
                YOU SLEPT FOR SO LONG, BUT YOU FEEL SOMETHING ITCHING YOUR LEG...
                OH NO!!!
                IT'S A SNAKE BITE
                YOU HAVE TO GET THE POISON OUT
            """)
            input("press enter to get the poison out")
            os.system("cls")
            print("""
                SORRY, YOU DIDN'T MAKE IT. YOU DIE
            """)
        elif oppp5 == 2:
            print("""
            THE TENT TOOK SO LONG TO MAKE RIGHT?
            YOU MUST BE TIRED...
            YOU SHOULD SLEEP
            """)
            input("press enter to sleep")
            os.system("cls")
            print("""
                GOOD MORNING!
                DID YOU SLEEP WE...
                WHAT IS THAT SOUND?
                IT'S A SHIP!!!!
                YOU HAVE TO CALL THEM TO SAVE YOU
            """)
            input("PRESS ENTER TO CALL THEM")
            os.system("cls")
            print("""
                THE PEOPLE ON THE SHIP SEE YOU AND COME FOR YOU
                CONGRATS! YOU HAVE BEEN SAVED!!!
            """)


def beach():
    print("""While searching around the beach you encounter a man.a sailor of your own ship,thrown into the sea because of drinking,he should help you.
    """)
    print("""a sailor of your own ship,thrown into the sea because of drinking,he should help you but he is drunk and angry.


         1-Beat him to sober up
         2-Talk to him
    """)
    opb1 = int(input("~"))
    os.system("cls")
    if opb1 == 1:
        print("""
        You try to talk to him but he gets more angry and stabs you with a sharp tip of a broken wine glass,he tries to help you when he realises but you die from bleeding.

        ENDING : DEATH(Drunken Sailor) 
        """)

    elif opb1 == 2:
        print("""You give a heavy punch to his face when he gets near,he falls to the sands,when he gets up he asks why did you punch him,then you tell him what happend and he accepts to help you.
            """)
        print("""You Two then go past the jungle and get a few man and guns from the city which you will use to take back your ship in the Dockyard and punish the traitors,sailing the high seas.
            
            
            
            ENDING: LIFE(The Captain and his Sailors)
            """)

def playsong():
    from playsound import playsound
    playsound('song.mp3')
