# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 08:32:16 2022

@author: David
"""

def listDict(l, d):
    assert isinstance(l, list) and isinstance(d, dict)
    assert all(isinstance(li, int) for li in l)
    assert len(l) == len(d)
    return {k:listval if listval in range(5,10) else -1 for k,listval in zip(d,l)}



la = [8,7,1]
dic = {1:2,2:1,3:2}

print(listDict(la,dic))