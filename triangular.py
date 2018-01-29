#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:09:40 2017

@author: thelma
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    for i in range(1,k+1):
        if i*(i+1)/2 == k:
            return True
    return False

print(is_triangular(1))