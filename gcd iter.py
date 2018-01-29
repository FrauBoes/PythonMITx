#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:18:14 2017

@author: thelma
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    ans = min(a,b)
    while a%ans != 0 and b%ans != 0:
        ans -= 1
    return ans

print(gcdIter(6,60))
        