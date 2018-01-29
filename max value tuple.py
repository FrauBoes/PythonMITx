#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:12:33 2017

@author: thelma
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    max_int = 0
    for element in t:
        if type(element) == int:
            if element > max_int:
                max_int = element
        else:
            if max_val(element) > max_int:
                max_int = max_val(element)
    return max_int
    
        
print(max_val(([[2, 1, 5], [4, 2], 6], ([2, 1], (7, 7, 5), 6))))