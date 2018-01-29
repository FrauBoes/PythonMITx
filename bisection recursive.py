#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:09:40 2017

@author: thelma
"""

def bisect_search(L, e):
    def bisect_search_helper(L, e, low, high):
        if high = low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid -1)
        else:
            return bisect_search_helper(L, e, mid +1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) -1)
                