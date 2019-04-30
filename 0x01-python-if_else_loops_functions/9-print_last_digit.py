#!/usr/bin/env python3
def print_last_digit(number):
    if number < 0:
        num = (number * -1) % 10
        print(num, end="")
        return (num)
    else:
        num = number % 10
        print(num, end="")
        return (num)
