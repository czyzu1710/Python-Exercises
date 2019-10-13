#!/usr/bin/python
#-*- coding: utf-8
bigFatNumber=str(input("Type in a really big number:\t"))
print("You typed in number with ",sum([1 for x in bigFatNumber if x=='0']),"zeros.")

