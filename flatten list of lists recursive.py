#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:32:41 2017

@author: thelma
"""

n = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(aList):
    flattened = []
    for item in (aList):
        if type(item) != list:
            flattened.append(item)
        else:
            flattened.extend(flatten(item))
    return flattened

print(flatten(n))