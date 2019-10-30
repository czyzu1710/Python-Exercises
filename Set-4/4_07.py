#!/usr/bin/python
#-*- coding: utf-8 -*-

def flatten(sequence):
    result = []
    for x in sequence:
        if isinstance(x,(list,tuple)):
            for y in flatten(x):
                result.append(y)
        else: 
            result.append(x)
    return result

 
L = [1,2,3,[6],[[3,6,3]],(1,2)]
print(flatten(L))
