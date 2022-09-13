from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("600x480")
add = []
multiply = []
sub = []
divide = []
to_sum=0
to_add = False
to_sub = False
to_multiply = False
to_divide = False
current = ""


def button_click(number):
    global current
    view.insert(END,number)
    current = view.get()
    print(current)


def button_add():
    global current
    add.append(current)
    view.delete(0,END)
    global to_add
    to_add= True


def button_multiply():
    global current
    global to_multiply
    multiply.append(current)
    view.delete(0,END)
    to_multiply = True
    print(multiply,"is the multiply")


def button_minus():
    global sub
    global current
    global to_sub
    sub.append(current)
    view.delete(0,END)
    to_sub = True
    print(sub)


def button_divide():
    global divide
    global to_divide
    global current
    divide.append(current)
    view.delete(0,END)
    to_divide = True


def button_equal():

    #Calling variables
    global to_sum
    global sub
    global add
    global multiply
    global divide
    global current
    global to_add
    global to_sub
    global to_multiply
    global to_divide
    #To add elemnts to the list that is entered at last
    if to_add == True:
        add.append(current)
    if to_multiply == True:
        multiply.append(current)
        print(f"Multiply list is {multiply}")
    if to_sub == True:
        sub.append(current)
    if to_divide == True:
        divide.append(current)

    view.delete(0,END)
    to_sum = 0
    #Passing Addition check
    if to_add == True:
        view.delete(0,END)
        for i in add:
            to_sum += int(i)
        view.insert(0, to_sum)
    #Passing multiply check
    if to_multiply == True:
        view.delete(0,END)
        product = 1
        for i in multiply:
            product *= int(i)
            print(product)
        view.insert(0,product)
    if to_sub == True:
        view.delete(0,END)
        diff = 0
        count = 1
        for i in sub:
            if count == 1:
                diff = int(i)
            else:
                diff -= int(i)
            count += 1
            print(diff)
        view.insert(0,diff)
    if to_divide == True:
        current = 1
        temp = 0
        for i in divide:
            if current == 1:
                temp = int(i)
            else:
                temp = temp / int(i)
            current += 1
        view.insert(0,temp)

    # resetting values to list
    add = []
    multiply = []
    sub = []
    divide = []
    to_add = False
    to_sub = False
    to_multiply = False
    to_divide = False
def button_clr():
    global add,multiply,sub,divide
    view.delete(0,END)
    # resetting values to list
    add = []
    multiply = []
    sub = []
    divide = []

#Buttons and labels defining:

view = Entry(root,borderwidth=5,)
button_1 = Button(root, text="1", padx=10, pady=10, command=lambda: button_click("1"))
button_2 = Button(root, text="2", padx=10, pady=10, command=lambda: button_click("2"))
button_3 = Button(root, text="3", padx=10, pady=10, command=lambda: button_click("3"))
button_4 = Button(root, text="4", padx=10, pady=10, command=lambda: button_click("4"))
button_5 = Button(root, text="5", padx=10, pady=10, command=lambda: button_click("5"))
button_6 = Button(root, text="6", padx=10, pady=10, command=lambda: button_click("6"))
button_7 = Button(root, text="7", padx=10, pady=10, command=lambda: button_click("7"))
button_8 = Button(root, text="8", padx=10, pady=10, command=lambda: button_click("8"))
button_9 = Button(root, text="9", padx=10, pady=10, command=lambda: button_click("9"))
button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: button_click("0"))
button_add = Button(root,text="+", padx=30, pady=10,command=button_add)
button_sub = Button(root,text="-",padx=10,pady=15,command=button_minus)
button_clr = Button(root,text="Clear",padx=22,pady=10,command=button_clr)
button_equal = Button(root,text="=",padx=30,pady=10,command=button_equal)
button_multiply = Button(root,text="X",padx=10,pady=15,command=button_multiply)
button_divide = Button(root,text = "÷",padx=10,pady=15,command=button_divide)

#Arranging buttons:

view.grid(row=0,column=1,columnspan=3,)

button_7.grid(row=1,column=1)
button_8.grid(row=1,column=2)
button_9.grid(row=1,column=3)

button_4.grid(row=2,column=1)
button_5.grid(row=2,column=2)
button_6.grid(row=2,column=3)

button_1.grid(row=3,column=1)
button_2.grid(row=3,column=2)
button_3.grid(row=3,column=3)

button_0.grid(row=4,column=1)
button_clr.grid(row=4,column=2,columnspan=2)
button_add.grid(row=5,column=1,)
button_equal.grid(row=5,column=2,columnspan=2)

button_multiply.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_divide.grid(row=3, column=4)

root.mainloop()