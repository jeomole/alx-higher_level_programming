#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for i in range(0, len(str)):
        if ((ord(str[i]) >= ord('a')) and (ord(str[i]) <= ord('z'))):
            upper = chr((ord(str[i])) - 32)
        else:
            upper = str[i]
        newstr += upper

    print("{}".format(newstr))
