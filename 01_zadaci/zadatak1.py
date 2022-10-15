# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 08:23:00 2022

@author: David
"""

def fun(x):
    assert all(isinstance(i, str) for i in x)
    return [i for i in x if len(i)>4]


x = ["testt","trststst","sd"]

print(fun(x))
        