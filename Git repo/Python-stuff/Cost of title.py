#User provides Width = w and height = h and the cost of single title
# Use the info provided to calculate area and the cost of it

while True:
    try:
        w = int(input("Enter the width of the floor to cover with tile(in meter): "))
        break
    except ValueError:
        print("Please enter the value in numbers!")

while True:
    try:
        h = int(input("Enter the height of the floor to cover with tile(in meter): "))
        break
    except ValueError:
        print("Please enter the value in numbers!")

while True:
    try:
        cost = int(input("Enter the cost of title for 1m(in rupees): "))
        break
    except ValueError:
        print("Please enter the value in numbers(Do not include the rupees sign)!")

area = w * h
area_cost = area * cost
print(f"For an area of {area} (in meter), and for the cost of tile for 1m {cost} rupees, the total cost would be: {area_cost} rupees")
#For 1m the cost and then find the area in meters and get the cost(area * cost)
