#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:42:29 2017

@author: thelma
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    L_work = sorted(L)

    while len(L_work) > 0 and L_work.count(max(L_work)) % 2 == 0:
        del L_work[-(L_work.count(max(L_work))):]
    
    if len(L_work) == 0:
        return None
    else:
        return max(L_work)

print(largest_odd_times([3, 3, 2, 0]))
