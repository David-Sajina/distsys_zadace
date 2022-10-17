# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:43:25 2022

@author: David
"""

def fun(p1,p2):
    assert(isinstance(p1, list) and isinstance(p2, list) or isinstance(p1, dict) and isinstance(p2, dict))
    if(isinstance(p1, list)):
        return p1+p2
    else:
        return p1 | p2
    
    
l1 = [1,2,1,2]
l2 = [3,2]

print(fun(l1,l2))
d1= {1:2,3:2}
d2= {5:2,4:1}

print(fun(d1,d2))