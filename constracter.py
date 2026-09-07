# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:53:15 2026

@author: NARESH
"""

class sample:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def read(self):
        print(self.name)
        print(self.age)
s1=sample("kprit",20)
s1.read()