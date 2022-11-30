# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 00:24:20 2022

@author: Beth_El 2
"""

def isleap(y):
    if y % 100 == 0:
        print("year %d is divisible by 4 but not by 100" %y )
        return False
    if y % 4 == 0:
        print("year %d is divisible by 4 but not by 100" %y )
        return True
    if y % 400 == 0:
        print("year %d is divisible by 4 but not by 100" %y )
        return True
    else:
        print("year %d is divisible by 4 but not by 100" %y )
        return False
    
    