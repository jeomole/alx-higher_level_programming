#!/usr/bin/python
import random
number = random.randint(-10, 10)

if (number < 0):
    print(f"{:d} is negative")
elif (number == 0):
    print(f"{:d} is zero")
elif (number > 0):
    print(f"{:d} is positive")
