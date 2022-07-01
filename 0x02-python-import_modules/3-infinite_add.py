#!/usr/bin/python3
from sys import argv

def main() -> None:
    sum = 0
    for index, num in enumerate(argv):
        if index > 0:
            num = int(num)
            sum += num
    print("{}".format(sum))

if __name__ == "__main__":
    main()
