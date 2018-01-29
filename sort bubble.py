#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:35:03 2017

@author: thelma
"""

test = [1,5,3,8,4,9,6,2]

def bubble_sort(L):
    swapped = True
    while swapped:
        swapped = False
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swapped = True
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
    return L

print(bubble_sort(test))