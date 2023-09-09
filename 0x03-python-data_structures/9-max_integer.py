#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    lgt = my_list[0]
    for num in my_list:
        if num > lgt:
            lgt = num
    return lgt
