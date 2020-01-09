#! /usr/bin/python
# -*- coding: utf-8 -*-
from random import uniform


def calc_pi(n, r=1):
    counter = 0
    for i in range(n+1):
        x = uniform(0, 1)
        y = uniform(0, 1)
        if (x*x + y*y) <= r:
            counter += 1

    return counter/n * 4

