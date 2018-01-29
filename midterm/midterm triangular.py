#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 14:20:39 2017

@author: thelma
"""
def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    n = 1
    x = k
    while True:
        if x == 0:
            return True
            break
        elif x < 0:
            return False
            break
        else:
            x -= n
            n += 1
    
print(is_triangular(1829))