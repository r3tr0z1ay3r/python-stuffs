import time
from function import *
def prime_check(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
        else:
            return True
while True:
    amt = input("Enter the number to get the primes till: ")
    if handle_value_error(amt):
        amt = handle_value_error(amt)
        break
n = [x for x in range(1,amt)]
primes = []
multiples = 2
while (multiples**2) <= len(n):
    for i in n:
        if i%multiples == 0:
            n.remove(i)
    if prime_check(multiples) == True:
        n.append(multiples)
    multiples += 1
n.sort()
print(f"The following are the primes under {amt}:")
print(*n,end=" ")