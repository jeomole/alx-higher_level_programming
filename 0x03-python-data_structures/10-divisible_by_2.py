#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        new_list = list(map((lambda x:
                            True if x % 2 == 0 else False), my_list))
        return new_list
