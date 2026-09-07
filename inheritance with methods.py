# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:05:59 2026

@author: NARESH
"""

class animal:
    def eat(self):
        print("animal eat food")
class dog(animal):
    def speak(self):
        print("dog bark")
d1=dog()
d1.eat()
d1.speak()