# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 01:24:58 2022

@author: Beth_El 2
"""

#import leap

def isleap(y):
    if y % 100 == 0:
        #print("year %d is divisible by 4 but not by 100" %y )
        return False
    if y % 4 == 0:
        #print("year %d is divisible by 4 but not by 100" %y )
        return True
    if y % 400 == 0:
        #print("year %d is divisible by 4 but not by 100" %y )
        return True
    else:
        #print("year %d is divisible by 4 but not by 100" %y )
        return False

#April, June, September,November has 30 days
#January, March, May, July, August, October, December has 31 days
#February leap year 29days
#February non-leap year 28days

    

if isleap(2012):
    Month2 = 29
    print("29")
else:
    Month2 = 28
    print("28")
    
if isleap(2012):
    Month1 = 31
    Month3 = 31
    Month4 = 30
    Month5 = 31
    Month6 = 30
    Month7 = 31
    Month8 = 31
    Month9 = 30
    Month10 = 31
    Month11 = 30
    Month12 = 31
   
if  Month1 == 30 or Month3 == 30 or Month5 == 30 or Month7 == 30 \
    or Month8 == 30 or Month10 == 30 or Month12 == 30:
    print("30")
else: 
    print("31")
    
isleap(2012)