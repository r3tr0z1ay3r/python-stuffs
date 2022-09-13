def add(a,b):
    return (a+b)
def sub(a,b):
    return(a-b)
def multi(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
def percent(value,percentage):
    perc = (percentage/100)*value
    return perc
def clear():
    print("\n"*20)
print("\t\t CALCULATOR \t\t")
while True:
    print("Welcome please choose what do u want to do!")
    while True:
        try:
            choice = int(input("    1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division \n 5 for percentage \n 6 to exit \n Enter your choice here: "))
            break
        except ValueError:
            print("Please choose a number!")
    if choice == 6:
        print("\t\tExiting...")
        break
    while choice != 6:
        if choice == 1:
            while True:
                try:
                    a = int(input("Please enter first  number to add!: "))
                    b = int(input("Please enter second  number to add!: "))
                    break
                except ValueError:
                    print("Please enter a number!")
            clear()
            print(f"The sum of the two numbers {a} and {b} is {add(a,b)}")
            break
        if choice == 2:
            while True:
                try:
                    a = int(input("Please enter first  number to subtract from!: "))
                    b = int(input("Please enter second  number to subtract!: "))
                    break
                except ValueError:
                    print("Please enter a number!")
            clear()
            print(f"The difference of the two numbers {a} and {b} is {sub(a,b)}")
            break
        if choice == 3:
            while True:
                try:
                    a = int(input("Please enter first  number to multiply!: "))
                    b = int(input("Please enter second  number to multiply!: "))
                    break
                except ValueError:
                    print("Please enter a number!")
            clear()
            print(f"The product of the two numbers {a} and {b} is {multi(a, b)}")
            break
        if choice == 4:
            while True:
                try:
                    a = int(input("Please enter first  number to divide with!: "))
                    b = int(input("Please enter second  number to divide!: "))
                    break
                except ValueError:
                    print("Please enter a number!")
            clear()
            print(f"The quotient of the two numbers {a} and {b} is {div(a, b)}")
            break
        if choice == 5:
            while True:
                try:
                    a = int(input("Please enter value to find the percentage!: "))
                    b = int(input("Please enter percentage to find!: "))
                    break
                except ValueError:
                    print("Please enter a number!")
            clear()
            print(f"The percentage of the two numbers {a} and {b} is {percent(a, b)}")
            break
        if choice == 6:
            print("\t\tExiting...")
            break