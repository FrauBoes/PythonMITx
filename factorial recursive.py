#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:28:45 2017

@author: thelma
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(100))