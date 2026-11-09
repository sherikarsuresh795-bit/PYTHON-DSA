# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:54:23 2026

@author: suresh
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def insertion(self, num):
        newNode = Node(num)

        if self.head is None:
            self.head = newNode
            self.temp = newNode
        else:
            self.temp.next = newNode
            self.temp = newNode

    def display(self):
        if self.head is None:
            print("empty")
            return

        temp = self.head

        while temp!=None:
            print(temp.data, end=" -> " )#if temp.next else ""
            temp = temp.next
        print()


sll = LinkedList()

size = int(input("Enter size: "))

for i in range(size):
    num = int(input("Enter number: "))
    sll.insertion(num)

sll.display()