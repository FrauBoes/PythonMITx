#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:23:05 2017

@author: thelma
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(1, 13):
    monthlyPayment = balance * monthlyPaymentRate
    balance -= monthlyPayment
    monthlyInterest = balance * (annualInterestRate/12)
    balance += monthlyInterest 
    
print("Remaining balance: " + str(round(balance, 2)))
