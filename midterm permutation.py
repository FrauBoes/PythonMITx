#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:22:56 2017

@author: thelma
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''

    L1 = [1, 'b', 1, 'c', 'c', 1]
    L2 = ['c', 1, 'b', 1, 1, 'c']
    count = 0
    answer = True

    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    elif len(L1) != len(L2):
        return False
    else:
        for item in L1:
            if L1.count(item) == L2.count(item):
                if L1.count(item) > count:
                    count = L1.count(item)
                    element_most = item
            else:
                answer = False
        if answer == False:
            return answer
        else:
            return (element_most, count, type(element_most))
            