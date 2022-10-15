# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 08:51:54 2022

@author: David
"""

def artikl(x):
    art = ["cijena","naziv","kolicina"]
    rez = {'ukupno': {'artikli':[], 'cijena': 0}}
    assert isinstance(x, list)
    assert all(isinstance(i, dict)for i in x)
    assert all(list(i.keys())== art for i in x )
    for i in x:
        rez['ukupno']['artikli'].append(i['naziv'])
        rez['ukupno']['cijena'] +=  i['kolicina'] * i['cijena']
    return rez


lista = [{"cijena":8,"naziv":"Kruh","kolicina":1}, {"cijena":13,"naziv":"Sok","kolicina":2}, {"cijena":7,"naziv":"Upaljac","kolicina":1}] 
print(artikl(lista))