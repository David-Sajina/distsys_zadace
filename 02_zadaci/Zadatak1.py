#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:41:59 2022

@author: david
"""
import asyncio
import os

async def afun1(list_param):
    await asyncio.sleep(0.2)
    return [{'naziv': i, 'velicina': (os.path.getsize(i))} for i in list_param]

def fun2(list_param):
    for i in list_param:
        fp = open(i,'w')
        for j in range(1,10000):
            fp.write(str(j)+ " ")
        fp.close()

async def main():
    imena_datoteka = ['datoteka1', 'datoteka2', 'datoteka3']
    for i in imena_datoteka:
        fp = open(i, 'w')
        fp.close()
    var1 = asyncio.create_task(afun1(imena_datoteka))
    fun2(imena_datoteka)
    await var1
    print(var1.result())


if __name__ == '__main__':
    asyncio.run(main())
    