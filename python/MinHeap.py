#!/usr/bin/env python
# -*- coding: gbk -*-
# File Name: MinHeap.py
# Author: weitao
# mail: weitao@sogou-inc.com

import os
import re
import sys

DEBUG=False

def p(str):
    if DEBUG:
        print str


class MinHeap:

    def __init__(self,heapsize):
        self.heapCapacity=heapsize
        self.heaplist=[]
        self.DEBUG=True

    def push(self,element):
        if len(self.heaplist)<self.heapCapacity:
            self.heaplist.append(element)
        else:
            if self.heaplist[0]<element:
                self.pop()
                self.push(element)
            else:
                return
        self.shiftup()

    def swap(self,index1,index2):
        p("SWAP\t"+str(self.heaplist[index1])+"-"+str(self.heaplist[index2]))
        tmp=self.heaplist[index1]
        self.heaplist[index1]=self.heaplist[index2]
        self.heaplist[index2]=tmp
    def pop(self):
        self.swap(0,len(self.heaplist)-1)
        self.heaplist.pop()
        i=0
        left=i*2+1
        right=i*2+2

        while right<self.heapCapacity-1:
            if self.heaplist[left]<self.heaplist[right]:
                if self.heaplist[left]<self.heaplist[i]:
                    self.swap(i,left)
                    i=left
                    left=i*2+1
                    right=i*2+2
                else:
                    return
            else:
                if self.heaplist[right]<self.heaplist[i]:
                    self.swap(i,right)
                    i=right
                    left=i*2+1
                    right=i*2+2
                else:
                    return
        if left<self.heapCapacity-1:
            if self.heaplist[left]<self.heaplist[i]:
                self.swap(i,left)
    def shiftup(self):
        i=len(self.heaplist)-1
        up=(i-1)/2
        if i>0:
            p(str(self.heaplist[i])+"-"+str(self.heaplist[up]))
        if i%2==0:
            if self.heaplist[i]>self.heaplist[i-1]:
                i=i-1
        while i>0:
            if self.heaplist[i]<self.heaplist[up]:
                self.swap(i,up)
                i=up
                up=(i-1)/2
                if i%2==0:
                    if self.heaplist[i]>self.heaplist[i-1]:
                        i=i-1
                else:
                    if i+1 < len(self.heaplist) and self.heaplist[i]>self.heaplist[i+1]:
                        i=i+1
            else:
                break

    def PrintHeap(self):
        for item in self.heaplist:
            print item
