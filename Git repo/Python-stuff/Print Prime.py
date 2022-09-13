primes = []
import sympy
prime_list = sympy.primerange(1,1000)
print("1")
while True:
    choice = input("Do you want the next prime number? (y/n): ")
    if choice == "y" or choice == "Y" or choice == "n" or choice == "N":
        pass
    else:
        while True:
            print("Please enter either y or n!")
            break
    if choice == "y" or choice == "Y":
        print(next(prime_list))
    elif choice == "n" or choice == "N":
        print("User has choosen to end!")
        break