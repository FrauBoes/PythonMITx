# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    result = 0
    check = False
    for char in s:
        if char.isdigit():
            result += int(char)
            check = True
    if check == False:
        raise ValueError
    return result
        
print(sum_digits("a;e00sd!"))