#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:11:19 2017

@author: thelma
"""

s = 'boobboobrboobybobobbobbobobobobbziboobbobobbobbbobobbo'
start = 0
end = 3
count = 0
while end <= len(s):
    if s[start:end] == "bob":
        count +=1
    start += 1
    end +=1
print("Number of times bob occurs is: " + str(count))