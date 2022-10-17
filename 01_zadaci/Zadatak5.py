# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:33:45 2022

@author: David
"""

tuple_list = [(121,"Ivan","Ivic"), (431,"Pero","Horvat"), (31,"Marija","Maric")]

def nova_lista(lista1):
    return sorted([{'id': x[0], 'ime': x[1], 'prezime': x[2]} for x in lista1 if x[1][0] == x[2][0]], key= lambda x: x['id']) 

print(nova_lista(tuple_list))
