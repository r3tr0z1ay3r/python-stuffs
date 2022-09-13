from function import *
import time

#Doesnt save in memory or in a database and is saved only for the current instance
#Can be implemented into a database to save data

#To add productt
def prod_gather(prod):
    product = {}
    id = {}
    quantity = {}
    if len(prod) == 0:
        prod = 1
    else:
        print("len of prod is",len(prod))
        prod = len(prod)
    print(f"prod is {prod}")
    while True:
        amt = input("Amount of items you want to add: ")
        if handle_value_error(amt):
            amt = handle_value_error(amt)
            break
    intial = prod
    final = prod +amt
    for x in range(intial , final+1):
        product[f"product{x}"] = input(f"Enter product{x} name: ")
        id[f"id{x}"] = input("Enter id of the product: ")
        quantity[f"quantityt{x}"] = input(f"Enter quantity of product{x}: ")
    return(product,id,quantity)
class Product:
    def __init__(self,product,id,quantity):
        self.product = product
        self.id = id
        self.quantity = quantity


product = {}
id = {}
quantity = {}

while True:
    print("\t\tPRODUCT INVENTORY MANAGEMENT!")
    print("\t1.View current stock 2.Update stock 3.Exit")
    choice = input("Enter your choice: ")

    if handle_value_error(choice):
        choice = handle_value_error(choice)
    if choice == 3:
        print("Exiting....")
        break

    while choice != 3:
        if choice == 1:
            if len(product) == 0:
                print("There is no products currently!")
                time.sleep(1)
                break
            else:
                print("The products in invetory are:\n")
                for i in product:
                    print(f"{product.get(i)}")
                    print("is/are available in inventory")
                    for j in quantity:
                        if quantity.get(j) == None:
                            pass
                        else:
                            print(f"{quantity.get(j)} is the quantity available!")
                    time.sleep(2)
                    print("\n" * 2)
                break
                print("\n" * 5)
        elif choice == 2:
            product,id,quantity = prod_gather(product)
            print("The given information is updated!")
            print(len(product))
            break