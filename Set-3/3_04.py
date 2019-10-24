#!/usr/bin/python
#-*- coding: utf8 -*-
import math

while True:
    try:
        lastval = input("Type in number or 'stop' to exit\n ")
        x = float(lastval)
        print("(", x, ",", math.pow(x,3),")")
    except ValueError:
        if lastval=="stop":
            break
        print("You were suposed to type in float or 'stop'! Try again:\n")
        continue

