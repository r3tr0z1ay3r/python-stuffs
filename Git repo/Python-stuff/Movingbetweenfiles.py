import os
import time
from function import *
def file_move():
    parent_path = os.path.dirname(os.getcwd())
    while True:
        temp_path = parent_path
        for i in os.listdir(parent_path):
            print("____________________________________________________")
            print("\t>",i)
            print("____________________________________________________")
        choice = input("1.Open a folder\n2.Open a file\n3.Create a new file\n4.Create a new folder\n5.Open and edit a file\n6.Exit\nEnter your choice here: ")
        choice = handle_value_error(choice)
        if choice == 1:
            while True:
                    path = input("Please choose a file from above and enter it: ")
                    if path in os.listdir(parent_path):
                        parent_path += path
                        break
                    else:
                        print("There is no such files in the list given above")
        elif choice == 2:
            while True:
                file_name = input("Please enter the file name to open: ")
                try:
                    if file_name in parent_path == False:
                        print(file_name)
                        print(parent_path)
                        print("There is no such file in this directory!")
                        time.sleep(5)
                        break
                    if ".txt" in file_name or ".py" in file_name:
                        current_open = open(file_name,"r",encoding="utf-8")
                        print("THE CONTENT OF THE FILES!")
                        print("_______________________________________________________")
                        print("\t",current_open.read())
                        print("_______________________________________________________")
                        choice2 = input("Do you want to go back?(y): ")
                        while True:
                            if choice2.lower() == "y":
                                print("Going back!")
                                break
                            else:
                                print("Please enter a y if you wish to leave")
                        break
                except:
                    print("Sorry an error occured while trying to open that file!")
                    choice2 = input("Do you wish to go back?(y/n): ")
                    if choice2.lower() == "y" or choice2.lower() == "n":
                        if choice2 == "y":
                            "Going back a step..."
                            break
                        if choice2 == "n":
                            pass
                else:
                    print("Sorry I can only open text files(.txt)")
                    choice2 = input("Do you want to go back?(y/n): ")
                    if choice2.lower() == "y" or choice2.lower() == "n":
                        if choice2 == "y":
                            "Going back a step..."
                            break
                        if choice2 == "n":
                            pass
        elif choice == 3:
            print("If the file already exists it will be overwritten!")
            file = input("Please enter a file name with the extension: ")
            temp_path += file
            while True:
                lines = input("Enter the number of lines you wish to add: ")
                if handle_value_error(lines):
                    lines = handle_value_error(lines)
                    break

            print("Enter contents you want to be written to the file below!")
            print("____________________________________________________________")
            content = " "
            for i in range(0,lines):
                content += input(" ") + "\n"
            e = open(file,mode="w")
            e.write(content)
            e.close()
        elif choice == 4:
            print("The file will be created in the current folder!")
            folder_name = input("Enter the name of the file: ")
            temp_path += folder_name
            if not os.path.exists(temp_path):
                os.makedirs(temp_path)
                print(f"File has been created in {temp_path}")
                break
            else:
                print("A file by that name already exists!")
                time.sleep(5)
        elif choice == 5:
            while True:
                file_name = input("Please enter the file name to open: ")
                try:
                    if file_name in parent_path == False:
                        print(file_name)
                        print(parent_path)
                        print("There is no such file in this directory!")
                        time.sleep(5)
                        break
                    if ".txt" in file_name or ".py" in file_name:
                        current_open = open(file_name,"r+",encoding="utf-8")
                        print("THE CONTENT OF THE FILES!")
                        print("_______________________________________________________")
                        print("\t",current_open.read())
                        print("_______________________________________________________")
                        print("Write the content you want to add to here: ")
                        print("_______________________________________________________")
                        to_update = input(" ")
                        print("_______________________________________________________")
                        print("Being written to the file.....")
                        current_open.write(to_update)
                        time.sleep(2)
                        while True:
                            choice2 = input("Do you want to go back?(y): ")
                            if choice2.lower() == "y":
                                print("Going back!")
                                break
                            else:
                                print("Please enter a y if you wish to leave")
                        break
                except:
                    print("Sorry an error occured while trying to open that file!")
                    choice2 = input("Do you wish to go back?(y/n): ")
                    if choice2.lower() == "y" or choice2.lower() == "n":
                        if choice2 == "y":
                            "Going back a step..."
                            break
                        if choice2 == "n":
                            pass
        elif choice == 6:
            print("Exiting!")
            break
        else:
            print("Please enter a number corresponding to your choice!")
            time.sleep(5)