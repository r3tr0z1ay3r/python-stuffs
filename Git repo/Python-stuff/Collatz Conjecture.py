while True:
    try:
        n = int(input("Enter the number to find the seq: "))
        if n <= 1:
            print("Please enter a number greater than one!")
            continue
        break
    except ValueError:
        print("Please enter a number!")
step_count = 0
while n != 1:
    if n%2 == 0:
        n = n/2
    else:
        n = (n*3)+1
    step_count+=1
print("The number of steps for the value to reach one using collatz conjecture is: {}".format(step_count))