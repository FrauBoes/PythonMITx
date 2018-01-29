#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 11:43:04 2017

@author: thelma
"""

test = [1,5,3,8,4,9,6,2]

def selection_sort(L):
    suffix_start = 0
    while suffix_start != len(L):
        for i in range(suffix_start, len(L)):
            if L[i] < L[suffix_start]:
                L[suffix_start], L[i] = L[i], L[suffix_start]
                print(L)
        suffix_start += 1
    return L

print(selection_sort(test))