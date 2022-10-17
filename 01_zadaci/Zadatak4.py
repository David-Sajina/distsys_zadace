# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 09:18:19 2022

@author: David
"""

l1= [1,2,3,4,5]
l2= [2,2,4,4,5]

def fun(r,t):
    assert(len(l1)==len(l2))
    return [x if x == t[i] else -1 for i,x in enumerate(r)]

print(fun(l1,l2))