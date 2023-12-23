# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 06:59:12 2023

@author: Pupil
"""

m="Я хочу пиццы, Леся хочет домой, Соня хочет спать, Аня хочет каникул"
def Anna(e):
    k=''
    for i in range(len(m)): 
        if m[i].isalpha():
            k+=m[i].swapcase()
        else:
            k+=m[i]
    print(k)
Anna(m)    