#!/usr/bin/python3
for num1 in range(0, 9):
    for num2 in range(1, 10):
        if (num1 < num2 and num1 != num2):
            print("{}{}".format(num1, num2), end="")
            if not(num1 == 8):
                print("{}".format(","), end=" ")
            else:
                print("{}".format("\n"), end="")
