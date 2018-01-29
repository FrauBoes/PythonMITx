#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:15:58 2017

@author: thelma
"""
def genPrimes():
    primes = []  #primes generated so far
    last = 1     #last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
            else:
                primes.append(last)
                yield last
  
p = genPrimes()

p.__next__()
