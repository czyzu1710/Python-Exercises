#!/usr/bin/python
#-*- coding: utf-8
def printNumbers(L):
    line = "".join(str(x) for x in L) 
    print(line)

printNumbers([2,3,1,6,7,12,99,342,167894])
