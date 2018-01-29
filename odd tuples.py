#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 13:17:39 2017

@author: thelma
"""

aTup = ('I', 'am', 'a', 'test', 'tuple')
newTup = ()
x = 0
for element in aTup:
    if x%2 == 0:
        newTup += (element,)
    x += 1
print(newTup)