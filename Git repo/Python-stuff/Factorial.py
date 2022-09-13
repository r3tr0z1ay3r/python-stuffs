def factorial(n):
    fact = 1
    for i in range(1,n):
        fact = fact*i
    return fact
print("\t\t THIS PROGRAM  WILL FIND THE FACTORIAL! ")
while True:
    try:
        fact = int(input("\t Enter the number to find the factorial of: "))
        break
    except ValueError:
        print("Please enter a number")
if fact < 0:
    print("\tThere is no factorial for negative numbers!")
elif fact == 0:
    print("\tThe factorial of 0 is 1")
else:
    print(f"\tThe factorial of {fact} is {factorial(fact+1)}")