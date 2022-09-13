to_test = [-4,6,5,9,1,-1]

#Fn to check the closest to 0 which is positive

def check_positive_lowest(num:list):
    current = 0
    while True:
        for i in num:
            if current == i:
                return current
        current += 1

#Fn to compare and find closest to 0 which is negative

def check_negative_lowest(num:list):
    current = 0
    negative = [n for n in num if n < 0]
    while True:
        for i in negative:
            if current == i:
                return current
        current -= 1

#Assigning lowest values
positive_lowest = check_positive_lowest(to_test)
negative_lowest = check_negative_lowest(to_test)

#Comparing all possibles cases
if positive_lowest == negative_lowest:
    print(f"The closest element to 0 in the list provided is: {positive_lowest}")
if abs(negative_lowest) < positive_lowest:
    print(f"The closest element to 0 in the list provided is: {negative_lowest}")
else:
    print(f"The closest element to 0 in the list provided is: {positive_lowest}")