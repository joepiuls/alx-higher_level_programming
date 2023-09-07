#!/usr/bin/python3
def print_last_digit(number):
    execution = 0
    if number < 0:
        number *= -1
    execution = 1
    last = number % 10
    if execution == 1:
        number *= -1
    print("{:d}".format(last), end="")
    return last
