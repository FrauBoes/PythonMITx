#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:08:56 2017

@author: thelma
"""
def polysum(n,s):
    """
    Input: Positive integers n and s. n is the number of sides of the 
    polygon and is larger than 2, s is the length of each side of the polygon.
    
    Returns a positive integer, the sum of the area and the square of the 
    perimeter of the polygon, rounded to 4 decimal places.
    """
    
    # Import math library.  
    import math
    
    # Define the area of the polgon as area.  
    area = (0.25*n*s**2) / math.tan(math.pi/n)
    
    # Define the square of the perimeter as squarePeri.  
    squarePeri = (n*s) ** 2
    
    # Return sum of area and squarePeri rounded to 4 decimal places.
    return round(area+squarePeri, 4)

    