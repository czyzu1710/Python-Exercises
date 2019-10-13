#!/usr/bin/python
#-*- coding: utf-8
line = input("Type in few words:\t").split()
print("The words you typed in alphabetically:\n",sorted(line,key=str.lower),"\n The words you typed in from the shortest to the longest\n",sorted(line,key=len))
