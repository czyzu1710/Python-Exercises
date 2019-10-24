#!/usr/bin/python
#-*- coding: utf-8 -*-

rulerLenght = int(input("Type in ruler lenght:\t"))
ruler = ["|"]
ruler.append("....|"*rulerLenght)
ruler.append("\n0")
for x in range(1,rulerLenght+1):
    ruler.append(str(x).rjust(5))

print("".join(ruler))

