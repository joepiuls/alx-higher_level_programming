#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            upper_case = chr(ord(i)-32)
        else:
            upper_case = i
        print("{}".format(upper_case), end='')
    print('')
