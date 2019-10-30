#!/usr/bin/python
#-*- coding: utf-8 -*-

def fibonacci(n):
    result = [0,1]
    for x in range(2,n):
        result[0] = result[0] + result[1]
        result[1] = result[0] + result[1]
    
    return result[1] 


print(fibonacci(4))
