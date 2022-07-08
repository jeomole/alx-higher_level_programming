#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, delete_value in list(a_dictionary.items()):
        if value == delete_value:
            a_dictionary.pop(key)
    return a_dictionary
