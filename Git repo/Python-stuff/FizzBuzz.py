"""
 numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number
and for the multiples of five print “Buzz”. For numbers which are multiples of both three
and five print “FizzBuzz”.
"""
import time
for i in range(1,101):
    print(f"The current number is {i}")
    if i % 3 == 0 and i % 5==0:
        print("FizzBuzz")
        continue
    if i%3 == 0:
        print("Fizz")
    if i%5 == 0:
        print("Buzz")
    time.sleep(1)