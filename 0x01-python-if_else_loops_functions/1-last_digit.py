#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if (number < 0):
    last = number % -10
    if (last != 0):
        print(f"Last digit of {n:d} is {last:d} and is less than 6 and not 0")
    else:
        print(f"Last digit of {n:d} is 0 and is 0")
else:
    last = number % 10
    if ((last) > 5):
        print(f"Last digit of {n:d} is {last:d} and is greater than 5")
    elif (last == 0):
        print(f"Last digit of {n:d} is 0 and is zero")
    elif (last < 6) and (last != 0):
        print(f"Last digit of {last:d} is {last:d} and is less than 6 and not 0")
