#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary) > 0:
        for person, score in a_dictionary.items():
            if score == max(a_dictionary.values()):
                return person
    return None
