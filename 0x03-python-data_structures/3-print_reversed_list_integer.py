#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for num in my_list:
        print("{:d}".format(num))
    # for i in range(-1, -(len(my_list) + 1), -1):
    # print("{:d}".format(my_list[i]))
