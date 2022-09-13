import os
import time
from function import *
MoveFile = __import__("Moving between files")
print("\t\t\t\t\tTEXT EDITOR!")
while True:
    print("\t1.Open a existing file\n\t2.Create a new file\n\t3.Exit the editor")
    choice = input("\tEnter your choice here: ")
    choice = handle_value_error(choice)
    if choice > 3:
        print("The value you have provided exceeds the options we have provided please enter a valid value!")
        continue
    if choice == 1:
        break