# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:59:10 2026

@author: NARESH
"""

class rectangle():
    def area(self,l,b):
        print(l*b)
    def perimeter(self,l,b):
        print(2*(l+b))
l=int(input("enter l="))
b=int(input("enter b="))
r=rectangle()
r.area(l,b)
r.perimeter(l,b)