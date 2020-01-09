#! /usr/bin/python
# -*- coding: -*-


def heron(a, b, c):
    if a + b > c and b + c > a and c + b > a:
        return ((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))**(1/2)/4
    else:
        raise ValueError
