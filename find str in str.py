#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:11:19 2017

@author: thelma
"""

s = 'azcbobobegghakl'  #Predefined str

count = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1
print('Number of times bob occurs is: ' + str(count))