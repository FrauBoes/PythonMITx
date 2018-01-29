#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:05:07 2017

@author: thelma
"""
"""
Calculate lowest monthly rate for credit to be paid off in 12 months '/'
using bisection search.
Input: positive int balance, positive float annualInterestRate
Output: lowest monthly rate as float, rounded to 2 decimals.
"""
balance = 320000    # Value given
annualInterestRate = 0.2   # Value given
low = balance / 12
high = balance * ((1+annualInterestRate/12)**12) / 12

while True:
    testbalance = balance
    guess = (high+low) / 2
    
    # Calculate total annual credit including interest
    for m in range(12):
        unpaid = testbalance - guess
        testbalance = unpaid + unpaid * annualInterestRate / 12

    # Bisection search
    if round(testbalance, 2) < 0:
        high = guess
        
    elif round(testbalance, 2) > 0:
        low = guess
        
    else:
        print('Lowest Payment: ' + str(round(guess, 2)))
        break