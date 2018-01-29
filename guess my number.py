#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:54:36 2017

@author: thelma
"""

high = 100
low = 0
print("Please think of a number between 0 and 100!")

while True:
    ans = (high+low)//2
    print("Is your secret number " + str(ans) + "?")
    number = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if number == "c":
        break
    elif number == "l":
        low = ans
    elif number == "h":
        high = ans
    else:
       print("Sorry, I did not understand your input.")
       
print("Game over. Your secret number was: " + str(ans))