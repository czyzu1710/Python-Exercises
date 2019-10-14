#!/usr/bin/python
#-*- coding: utf-8

def addZeros(L):
   print([str(x).zfill(3) for x in L])

addZeros([1,2,3,22,123,67,33])


