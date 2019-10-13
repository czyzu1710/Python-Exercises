#!/usr/bin/python
#-*- coding: utf-8
line = input("Type in few words:\t").split()
print("Combined length of words You typed in is: ", sum(len(x) for x in line ))


