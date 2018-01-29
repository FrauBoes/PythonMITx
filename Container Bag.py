#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 11:40:37 2017

@author: thelma
"""

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            None

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        try:
            return self.vals[e]
        except:
            return 0
    
    def __add__(self, other):
        s = ""
        dict_sum = {}
        for i in sorted(self.vals.keys()):
            dict_sum[i] = self.vals[i]
        for j in sorted(other.vals.keys()):
            if j in dict_sum:
                dict_sum[j] += other.vals[j]
            else:
                dict_sum[j] = other.vals[j]
        for k in dict_sum:
            s += str(k)+":"+str(dict_sum[k])+"\n"
        return s



# print 3:1, 4:2
a = Bag()
a.insert(4)
b = Bag()
b.insert(4)
a.insert(3)
a.remove(3)
print(a+b)
