# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 06:56:13 2023

@author: Pupil
"""

b=[]
n='щука ест Георгия'
m="Олеся жрёт жаренную щуку"
def vika():
    dd=n.rfind(m)
    if dd!=-1:
        b.append(dd)
    else:
        b.append("Иди за щукой")
    print(b)
vika()