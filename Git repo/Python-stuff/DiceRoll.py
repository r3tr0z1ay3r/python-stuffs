#DICE SIMULATION
import random
import time
def spin_die():
    print("Rolling the dice...")
    roll = random.randint(1,6)
    time.sleep(2)
    print(f"The dice landed on {roll}")
print("\t\tDICE SIMULATION PROGRAM!")
while True:
    choice = input("Do you want to roll the dice?(y/n)")
    if choice.lower() == "y":
        spin_die()
    elif choice.lower() == "n":
        print("Exiting the program!")
        break
    else:
        print("Please provide y or n!")