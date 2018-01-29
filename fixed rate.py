#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:23:31 2017

@author: thelma
"""

balance = 3329
annualInterestRate = 0.2
lowestPayment = 10

while True:
    testbalance = balance
    
    for m in range(1,13):
        unpaid = testbalance - lowestPayment
        testbalance = unpaid + unpaid * annualInterestRate / 12
#        if testbalance <= 0:
#            break
        
    if testbalance <= 0:
        print('Lowest Payment: ' + str(lowestPayment))
        break
    
    lowestPayment += 10