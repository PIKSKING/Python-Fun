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





