#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:30:50 2017

@author: thelma
"""
s = 'azcbobobegghakl'

num = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        num += 1
print("Number of vowels: " + str(num))