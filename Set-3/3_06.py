#!/usr/bin/python
#-*- coding: utf-8 -*-

height = int(input("Type in height of rectangle:\n"))
width = int(input("Type in width of rectangle:\n"))

horizontalEdge="+" + "---+"*width
verticalEdge="\n|" + "|".rjust(4)*width +"\n"
rectangle=horizontalEdge + (verticalEdge+horizontalEdge)*height

print(rectangle)
