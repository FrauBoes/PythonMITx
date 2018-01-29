#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:17:07 2017

@author: thelma
"""

x = 9
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + x
    itersLeft -= 1
print(str(x) + "*" + str(x) + "=" + str(ans))