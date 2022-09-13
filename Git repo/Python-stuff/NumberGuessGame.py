import time
import random
from function import *
print("\t\tWELCOME TO NUMBER GUESSING GAME!")
while True:
    print("I will think of a number between 1 to 10!\nTry and guess the number :)")
    correct_no = random.randint(1,10)
    time.sleep(2)
    print("I have thought of an number!")
    while True:
        guess = input("Enter your guess: ")
        if handle_value_error(guess):
            guess = handle_value_error(guess)
            break
    if correct_no == guess:
        print("How did you-")
        print("I mean CONGRATULATION you won!")
    elif correct_no != guess:
        print("Bzzzzt!")
        print("Sorry but you lost!")
        print(f"The number that i thought of was {correct_no}")
    choice = input("Do you want to play again?(y/n)")
    if choice.lower() == "y":
        print("Restarting the game...")
        time.sleep(1)
        print("\n"*10)
        continue
    if choice.lower() == "n":
        print("Exiting the game!")
        time.sleep(1)
        break
    else:
        print("Please enter y or n!")