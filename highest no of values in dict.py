#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 13:37:40 2017

@author: thelma
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

result = None
biggestValue= 0
for key in animals.keys():
    if len(animals[key]) >= biggestValue:
        result = key
        biggestValue = len(animals[key])
print(result)
    
        