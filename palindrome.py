#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 16:18:54 2017

@author: thelma
"""

def isPalindrome(s):
    """
    s: str
    output: True if s is a Palindrome, otherwise False.
    """
    def toChars(s):
        """
        turn s into all lower characters and remove any non characters  
        """    
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans
    
    def isPal(s):
        """
        check to see if s is a palindrome by moving from outside to inside    
        5"""    
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))

print(isPalindrome("Madam, I am Adam"))
