#!/usr/bin/python3
from sys import argv


def main() -> None:
    length = len(argv)
    sing = "argument"
    plural = "arguments"

    print("{} {}".format(length - 1,
                         sing if length == 2 else plural), end="")
    print("{}".format("." if length == 1 else ":"))

    for i in range(1, length):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
