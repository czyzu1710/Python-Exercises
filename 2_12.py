#!/usr/bin/python
#-*- coding: utf-8

line = input("Type in few words:\t").split()
print("First letters create a word:\t", "".join([x[0] for x in line]),"\nLast letters create a word:\t", "".join(x[len(x)-1] for x in line))
