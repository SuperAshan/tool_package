#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File Name: HeapTest.py
# Author: weitao
# mail: weitao@sogou-inc.com

import os
import re
import sys
from MinHeap import MinHeap


class heapitem:

    def __init__(self,data=None,key=None):
        self.data=data
        self.key=key

    def __cmp__(self,other):
        if other.key > self.key:
            return -1
        elif other.key < self.key:
            return 1
        else:
            return 0
    def __repr__(self):
        return "(%s,%s)" % (self.data,str(self.key))


heap=MinHeap(8)
a=heapitem("我的",3)
b=heapitem("你的",4)
c=heapitem("天下",1)
d=heapitem("发放机",10)
e=heapitem("是打飞机安居房",6)
f=heapitem("是打安居房",2)
print a
heap.push(a)
print b
heap.push(b)
print c
heap.push(c)
print d
heap.push(d)
print e
heap.push(e)
print f
heap.push(f)

heap.PrintHeap()






