#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    key_is_a_string = type(key) == str
    if key_is_a_string:
        a_dictionary[key] = value
    return a_dictionary
