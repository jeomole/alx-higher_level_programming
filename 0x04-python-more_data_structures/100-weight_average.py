#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        score_total = 0
        weight_total = 0
        for elem in my_list:
            score_total += (elem[0] * elem[1])
            weight_total += elem[1]
        return score_total / weight_total
