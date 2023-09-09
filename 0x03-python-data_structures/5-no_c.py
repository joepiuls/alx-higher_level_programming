#!/usr/bin/python3
def no_c(my_string):
    result = []
    for leta in my_string:
        if leta != 'c' and leta != 'C':
            result.append(leta)
    return ''.join(result)
