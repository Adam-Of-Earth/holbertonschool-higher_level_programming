#!/usr/bin/python3
def no_c(my_string):
    ret = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            ret += i
    return ret
