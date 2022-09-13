from tkinter import *
from tkinter import messagebox
import random
import time

root = Tk()
root.title("Rock Paper Scissor Game")
root.geometry("640x480")

all_options = ["Rock","Paper","Scissor"]
player_chosen = StringVar()
player_chosen.set("Rock")
player_choice = ""
result = ""

#Functions
#Computer side
def comp_turn():
    choice = random.randint(0,2)
    chosen = all_options[choice]
    print(chosen)
    return chosen


#Player side
def returnChoice():
    global player_choice
    player_choice = player_chosen.get()

#Check win 
def winCheck():
    global computer_choice
    global player_choice
    comp.delete(0,END)
    computer_choice = comp_turn()
    player_choice = player_chosen.get()
    
    #Rock Instances
    if player_choice == "Rock" and computer_choice == "Rock":
        result = "Tie!"
        comp.insert(0,computer_choice)
    if player_choice == "Rock" and computer_choice == "Paper":
        result = "Player Wins!"
        comp.insert(0,computer_choice)
    if player_choice == "Rock" and computer_choice == "Scissor":
        result = "Player Wins!"
        comp.insert(0,computer_choice)
    
    #Paper Instances
    if player_choice == "Paper" and computer_choice == "Paper":
        result = "Tie!"
        comp.insert(0,computer_choice)
    if player_choice == "Paper" and computer_choice == "Rock":
        result = "Computer Won!"
        comp.insert(0,computer_choice)
    if player_choice == "Paper" and computer_choice == "Scissor":
        result = "Computer Won!"
        comp.insert(0,computer_choice)
    
    #Scissor Instances
    if player_choice == "Scissor" and computer_choice == "Scissor":
        result = "Tie!"
        comp.insert(0,computer_choice)
    if player_choice == "Scissor" and computer_choice == "Paper":
        result = "Player won!"
        comp.insert(0,computer_choice)
    if player_choice == "Scissor" and computer_choice == "Rock":
        result = "Computer Won!"
        comp.insert(0,computer_choice)

    else:
        print("Current choice is not enuf nubby")
    print(f"computer picked {computer_choice} and you picked {player_choice}")
    messagebox.showinfo("Result of round!",result)
    computer_choice = ""
    player_choice = ""
    


#Defining and griding buttons and labels

#Labels
#Computer stuff
computer_choice = comp_turn()
comp_lab = Label(root,text="Computer's chosen: ")
comp_lab.grid(row=1,column=0)
comp = Entry(root,width=10)
comp.grid(row=1,column=1)

#Player stuff
player_lab = Label(root,text="Your Choice: ")
player_lab.grid(row=0,column=0)
player_entry = OptionMenu(root,player_chosen,*all_options)
player_entry.grid(row=0,column=1)

submit_btn = Button(root,text="Submit Choice",command=winCheck)
submit_btn.grid(row=0,column=3,columnspan=2)





root.mainloop()