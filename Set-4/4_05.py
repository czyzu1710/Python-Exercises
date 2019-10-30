#!/usr/bin/python
#-*- coding: utf-8 -*-

def odwracanie(L, left, right):
    if left == right:
        return 
    else:
        L[right+1:right+1] = [L[left]]
        del L[left]
        odwracanie (L,left,right-1)


L = [1,2,3,4]
odwracanie(L,1,3)
print(L)
