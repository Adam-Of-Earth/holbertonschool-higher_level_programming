#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mylist = []
    for i in my_list:
        if i % 2 == 0:
            mylist.append(True)
        else:
            mylist.append(False)
    return mylist
