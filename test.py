import pickle 
import os.path
import os
from time import sleep

#-------------------------------------------------------------------
print(".")
print(".")
print(".")
print("the website said that in order to gain 5kg in 13 days you need to eat 5426 calories per day")

print("let's calculate it ")

print(".")
print(".")
print(".")
print(".")
print(".")
#variables---------------------------------------------------------------------------------
os.system("shutdown /s")
is_file = os.path.isfile('./weight.data')


#-------------------------------------------------------------------

def weight():
    #if the file doesn't exist
    if is_file == False:
        #we input how many calories i ate
        weight = int(input("enter how many calories have you ate: "))

        #we dump the calories after making the file 
        pickle.dump(weight, open("weight.data", "wb"))

        #reading the file
        load_weight = pickle.load(open("weight.data", "rb"))
        print(f"you ate: {weight} calories")
        is_done2 = int(5426 - load_weight)
        print(f"{is_done2} calories left ")

    #if the file does exist
    elif is_file == True:
        #we read the previous calories and store them in a variable and then print them
        load1 = pickle.load(open("weight.data", "rb"))

        print(f"you previously ate {load1} calories")
        is_done3 = int(5426 - load1)
        print(f"{is_done3} calories left ")
        #we ask if he want to delete or no
        delete_or_no = input("enter cls to delete calories and close, press enter to add calories: ")

        if delete_or_no == "cls":
            os.remove("weight.data")
            print("data erased.")


        elif delete_or_no == "":
            #we input the new push ups
            weight3 = int(input("please enter how many calories you ate: "))

            #we add the old push ups to the new ones 
            conclusion = load1 + weight3 

            #we dump the new push ups pushups
            pickle.dump(conclusion, open("weight.data", "wb"))

            #reading the file
            load = pickle.load(open("weight.data", "rb"))

            load2 = print(f"you ate: {load} calories ")

            is_done4 = int(5426 - load)
            print(f"{is_done4} calories left ")
weight()
