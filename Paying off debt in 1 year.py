#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:25:24 2017

@author: thelma
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(1, 13):
    monthlyPayment = balance * monthlyPaymentRate
    balance -= monthlyPayment
    monthlyInterest = balance * (annualInterestRate/12)
    balance += monthlyInterest 
    
print("Remaining balance: " + str(round(balance, 2)))
