#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:35:03 2017

@author: thelma
"""

test = [1,5,3,8,4,9,6,2]

def bogo_sort(L):
    while not is.sorted(L):
        random.shuffle(L)
    return L

print(bogo_sort(test))