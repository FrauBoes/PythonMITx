#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:23:38 2017

@author: thelma
"""
s = 'afhduakdhsjdhe'

current_String = s[0]
longest_String = s[0]

for i in range (len(s)-1):
    if s[i] <= s[i+1]:
        current_String += s[i+1]
        if len(current_String) > len(longest_String):
            longest_String = current_String
    else:
        current_String = s[i+1]
print("Longest subs in alphabetical order is: ", longest_String)