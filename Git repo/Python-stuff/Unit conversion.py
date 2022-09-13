def dol_to_inr(dollar):
    inr = 75
    print(f"{dollar}$ in rupees will be {dollar * inr}₹ approximately")
def inr_to_dol(rupees):
    dollar =   0.013
    print(f"{rupees}₹ in dollar will be {dollar * rupees}$ approximately")
def cel_to_far(cel):
    faren = (cel*(9/5))+32
    print(f"{cel}°C in farenheit will be {faren}°F")
def far_to_cel(far):
    cel = (far-32)*(5/9)
    print(f"{far}°F in celsius will be {cel}°C " )
def cm_to_inch(cm):
    print(f"{cm}cm in inch will be {round((cm/2.54),2)}inches")
def inch_to_cm(inch):
    print(f"{inch}inch in centimeter will be {round((inch*2.54),2)}cm")
def inch_to_feet(inch):
    print(f"{inch}inch in feet will be {round((inch/12),2)}ft")
def feet_to_inch(feet):
    print(f"{feet}ft in inches will be {round((feet*12),2)}inches")
def feet_to_cm(feet):
    print(f"{feet}ft in centimeter will be {round((feet*30.48,2))}cm")
def cm_to_feet(cm):
    print(f"{cm}cm in feet will be {round((cm/30.48),2)}ft")
print("\t\t\t WELCOME TO UNIT CONVERSION!")
print("\tI can convert from and in the followings units...\n1. Dollar\n2. Rupees\n3. Celsius\n4. Farenheit\n5. Centimeter\n6. Inch\n7. Feet")
from_unit = input("\t Please enter the unit you want to convert:  ")
to_unit = input("\t Please enter the unit you want to convert to: ")
from_unit = from_unit.lower()
to_unit = to_unit.lower()
if from_unit == "dollar":
    if to_unit == "rupees":
        while True:
            try:
                dol = int(input("Enter the dollar to convert to rupees(without symbol): "))
                break
            except ValueError:
                print("Please enter a valid value!")
        dol_to_inr(dol)
    else:
        print("Sorry I can only convert dollar to rupees or vice versa!")
if from_unit == "rupees":
    if to_unit == "dollar":
        while True:
            try:
                rup = int(input("Enter the rupees to convert to dollar(without symbol): "))
                break
            except ValueError:
                print("Please enter a valid value!")
        inr_to_dol(rup)
    else:
        print("Sorry I can only convert rupees to dollar or vice versa!")
if from_unit == "celsius":
    if to_unit == "farenheit":
        while True:
            try:
                cel = int(input("Enter the celsius to convert to farenheit(without symbol): "))
                break
            except ValueError:
                print("Please enter a valid value!")
        cel_to_far(cel)
    else:
        print("I can only convert from celsius to farenheit and vice versa!")
if from_unit == "farenheit":
    if to_unit == "celsius":
        while True:
            try:
                far = int(input("Enter the farenheit to convert to celsius(without symbol): "))
                break
            except ValueError:
                print("Please enter a valid value!")
        far_to_cel(far)
    else:
        print("I can only convert from farenheit to celsius and vice versa!")
if from_unit == "centimeter":
    if to_unit == "inch":
        while True:
            try:
                cm = int(input("Enter the centimeter to convert to inch(without symbol): "))
                break
            except ValueError:
                print("Please enter a valid value!")
        cm_to_inch(cm)
    if to_unit == "feet":
        while True:
            try:
                cm = int(input("Enter the centimeter to convert to feet(without symbol): "))
                break
            except ValueError:
                print("Please enter a valid value!")
        cm_to_feet(cm)
    else:
        print("I can only convert centimeter to inch or feet")
if from_unit == "inch":
    if to_unit == "centimeter":
        while True:
            try:
                inch = int(input("Enter the inch to convert to centimeter(without symbol): "))
                break
            except ValueError:
                print("Please enter a valid value!")
        inch_to_cm(inch)
    else:
        print("I can only convert from inch to centimeter and vice versa")
if from_unit == "inch":
    if to_unit == "feet":
        while True:
            try:
                inch = int(input("Enter the inch to convert to feet(without symbol): "))
                break
            except ValueError:
                print("Please enter a valid value!")
        inch_to_feet(inch)
    else:
        print("I can only covert inch to either feet or centimeter!")
if from_unit == "feet":
    if to_unit == "inch":
        while True:
            try:
                feet = int(input("Enter the feet to convert to inch(without symbols): "))
                break
            except ValueError:
                print("Please enter a valid value!")
        feet_to_inch(feet)
    if to_unit == "centimeter":
        while True:
            try:
                feet = int(input("Enter the feet to convert to centimeter(without symbols): "))
                break
            except ValueError:
                print("Please enter a valid value!")
        feet_to_cm(feet)
    else:
        print("I can only convert feet into inch or centimeter ")