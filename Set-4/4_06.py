#!/usr/bin/python
#-*- coding: utf-8 -*-

def sum_seq(sequence):
    result = 0
    for x in sequence:
        if isinstance(x,(list,tuple)):
            result += sum_seq(x)
        else: 
            result += x
    return result

 
L = [1,2,3,[6],[[3,6,3]],(1,2)]
print(sum_seq(L))
