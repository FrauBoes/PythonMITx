#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:58:24 2017

@author: thelma
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
        
    def __repr__(self):
        return str(self)

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
