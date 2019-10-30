#!/usr/bin/python
#-*- coding: utf-8 -*-
def ruler1():
    rulerLenght = int(input("Type in ruler lenght:\t"))
    ruler = ["|"]
    ruler.append("....|"*rulerLenght)
    ruler.append("\n0")
    for x in range(1,rulerLenght+1):
        ruler.append(str(x).rjust(5))

    return "".join(ruler)


def ruler2(rulerLength):
    ruler = ["|"]
    ruler.append("....|"*rulerLength)
    ruler.append("\n0")
    for x in range(1,rulerLength+1):
        ruler.append(str(x).rjust(5))

    return "".join(ruler)


print(ruler2(12))
print(ruler1())


