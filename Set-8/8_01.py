#! /usr/bin/python
# -*- coding: utf-8 -*-

# y= -a / b * x -c/b
def solve1(a: float, b: float, c: float) -> tuple:
    y = -c / b
    x = (b * y + c) / -a
    return x, y


