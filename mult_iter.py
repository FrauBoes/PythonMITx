#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:52:59 2017

@author: thelma
"""

def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
        print (result, b)
    return result

print(mult_iter(6,6))