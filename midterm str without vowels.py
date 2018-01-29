#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:30:50 2017

@author: thelma
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''

    s = 'a'
    answer = '' 
    for x in s:
        if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u' and x != 'A' and x != 'E' and x != 'I' and x != 'O' and x != 'U':
            answer += x 
    print(answer)

print_without_vowels("Julia ist klasse bombe")