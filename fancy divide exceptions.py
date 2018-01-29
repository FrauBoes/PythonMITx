# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        item / denom
    except ZeroDivisionError:
        return 0
    else:
        return item / denom

print(fancy_divide([0, 2, 4], 0))