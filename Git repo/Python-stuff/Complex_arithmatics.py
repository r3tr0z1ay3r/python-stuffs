#complex number x+iy
import re
from function import *
complex_no = "8+7i"

#Partially incomplete Need to fix sign error in multiply

#definitions of fns

def complex_split(complex_no):
    no = []
    no_int = []
    extras = []
    for i in complex_no:
        if i == "+" or i == "-":
            extras.append(i)
        try:
            if int(i):
                no.append(i)
        except ValueError:
            continue
    for i in extras:
        if i == "+" or i == "-":
            symbol = i
        else:
            raise NotImplementedError
    for i in range(0,len(no)):

        if i == 1:
            no[1] = symbol + no[i]
    for i in no:
        num = int(i)
        no_int.append(num)
    return [no_int,extras]

def complex_check(comp):
    pattern = "\d[+|-]\di"
    if re.search(pattern,comp):
        return True
    else:
        return False

def sym_def(sym1,sym2,num1,num2):
    sym1 = sym1[0]
    sym2 = sym2[0]
    real1,imag1 = num1
    real2,imag2 = num2

    if sym1 == "+" and sym2 == "+":
        symbol = "+"
    elif sym1 == "-" and sym2 == "+" and imag1 > imag2:
        symbol = "-"
    elif sym2 == "-" and sym1 == "+ "and imag2 > imag1:
        symbol = "-"
    elif sym1 == "-" and sym2 == "-":
        symbol = ""
    else:
        symbol = "+"
    return(symbol)

def add_complex(comp1,comp2,symbol):
    real_part1, imaginary_part1 = comp1
    real_part2, imaginary_part2  = comp2
    real_part_sum = real_part1 + real_part2
    imaginary_part_sum = imaginary_part1 + imaginary_part2
    return_list = []
    return_list.append(real_part_sum)
    return_list.append(imaginary_part_sum)
    real_part,imaginary_part = return_list
    print(f"Result of it is, {real_part} {symbol} {imaginary_part} i")


def multi_complex(comp1,comp2):
    comp1_list = []
    comp2_list = []
    numbs1_list = []
    numbs2_list = []
    numbs1 = []
    numbs2 = []
    sym1 , sym2 = [] , []
    to_work = []
    i_list = []
    for i in comp1:
        comp1_list.append(i)
    for i in comp2:
        comp2_list.append(i)
    for i in comp1_list:
        if i.isdigit():
            numbs1_list.append(i)
        else:
            if i == "+" or i == "-":
                sym1.append(i)
            if i == "i":
                i_list.append(i)
    for i in comp2_list:
        if i.isdigit():
            numbs2_list.append(i)
        else:
            if i == "+" or i == "-":
                sym2.append(i)
            if i == "i":
                i_list.append(i)


    if sym1[0] == "-":
        numbs1_list[1] = "-"+numbs1_list[1]
        symbol_check1 = True
    else:
        symbol_check1 = False
    if sym2[0] == "-":
        numbs2_list[1] = "-" + numbs2_list[1]
        symbol_check2 = True
    else:
        symbol_check2 = False
    for i in numbs1_list:
            numbs1.append(int(i))

    for i in numbs2_list:
            numbs2.append(int(i))

    for i in numbs1:
        for j in numbs2:
            to_work.append(i*j)

    if len(i_list) == 2:
        to_work[3] = -to_work[3]
    real = to_work[0] + to_work[3]
    imag = to_work[1] + to_work[2]
    if symbol_check2 == True:
        symbol = ""
    else:
        symbol = "+"
    print(f"The product of the complex number {comp1} and {comp2} is: {real}{symbol}{imag}i")


#Start of programs


while True:
    choice = input("1.Add or Subtract 2.Multiply  3.Exit \nEnter your choice: ")
    if handle_value_error(choice):
        choice = handle_value_error(choice)
    else:
        continue

    if choice == 1:
        print("Please provide proper value that can be added!")
        to_work1 = input("Enter a complex number(x+yi): ")
        if complex_check(to_work1):
            to_work1 = to_work1
        else:
            print("The value provided is not a complex number!")
            continue
        to_work2 = input("Enter another complex number(x+yi): ")
        if complex_check(to_work2):
            to_work2 = to_work2
        else:
            print("The value provided is not a complex number!")
            continue
        to_work1, sym1 = complex_split(to_work1)
        to_work2, sym2 = complex_split(to_work2)
        symbol = sym_def(sym1, sym2, to_work1, to_work2)
        print("\n" * 10)
        add_complex(to_work1,to_work2,symbol)
        print("\n"*2)
    if choice == 2:
        print("Please provide proper values !")
        to_work1 = input("Enter a complex number(x+yi): ")
        to_work2 = input("Enter another complex number(x+yi): ")
        print("\n" * 10)
        multi_complex(to_work1,to_work2)
        print("\n" * 2)
    if choice == 3:
        print("Exiting...")
        break