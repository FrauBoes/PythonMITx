#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 12:02:39 2017

@author: thelma
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    L_work = L[:]

    def poly(x):
        count = 0
        answer = 0
        while len(L_work) > 0:
            answer += (L_work.pop()*x**count)
            count += 1
        return answer
    
    return poly

general_poly([1,2,3,4])