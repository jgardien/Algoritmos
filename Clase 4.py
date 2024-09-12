# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 14:35:14 2019

@author: Azul
"""

def potencia(a,n):
    
    if n==0:
        rv=1
    else:
        rv=a*potencia(a,n-1)
    return rv

def suma(l):
    if len(l)==0:
        rv=0
    else:
        rv=l[0]+suma(l[1:])
    return rv

def maximo(l):
    if len(l)==1:
        return l[0]
    else:
        rv=maximo(l[1:])
        return rv if rv > l[0] else l[0]


print (potencia(2,6))
l=[0,1,22,3,4,5,6]
print (l,suma(l))
print(maximo(l))