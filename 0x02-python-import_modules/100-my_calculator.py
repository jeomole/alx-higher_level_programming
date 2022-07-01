#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, div, mul


def main():
    """Entry of calculator program
        returns 0 on success
        1 otherwise"""

    if len(argv) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator_checker = 0
    operator_list = ['+', '-', '*', '/']
    for operator in operator_list:
        if argv[2] == operator:
            operator_checker += 1

    if operator_checker == 0:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
        # exit breaks out of loop and program

    if argv[2] == '+':
        print(f"{a:d} + {b:d} = {add(a, b):d}")
    if argv[2] == '-':
        print(f"{a:d} - {b:d} = {sub(a, b):d}")
    if argv[2] == '*':
        print(f"{a:d} * {b:d} = {mul(a, b):d}")
    if argv[2] == '/':
        print(f"{a:d} / {b:d} = {div(a, b):d}")

    return 0


if __name__ == "__main__":
    main()
