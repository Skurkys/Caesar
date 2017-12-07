#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:51:01 2017

@author: sku35268
"""

x = input("Caesarova šifra")
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p = input("Zadej číslo>>>")
p = int(p)
b = a[p:] + a[:p]
t = input("Zadej text>>>")
t = int(t)


for znak in t:
    znak = znak + p
    
print(t)

