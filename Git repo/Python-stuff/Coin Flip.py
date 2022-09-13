#coin flip sim
import random
import time
print("\t\t THIS PROGRAM WILL SIMULATE A COIN FLIP NUMBER OF TIMES PROVIDED!")
while True:
    try:
        n = int(input("\tNumber of tries to flip the coin: "))
        break
    except ValueError:
        print("Please enter a valid value!")
while True:
    while True:
        choice = input(f"Do you want {n}  flips? (y/n): ")
        if choice.lower() == "y" or choice.lower() == "n":
            break
        else:
            print("Please enter y or n!")
    if choice == "y":
        for i in range(1,n+1):
            print(f"\tFlip number {i}")
            rand = random.randint(1,10)
            if rand % 2 == 0:
                print("HEADS!")
            else:
                print("TAILS!")
            if n == 1:
                pass
            else:
                print("\tTossing again...")
            time.sleep(2)
    else:
        print("Exiting the program...")
        break