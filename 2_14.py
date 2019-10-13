#!/usr/bin/python
#-*- coding: utf-8

line = sorted(input("Type in few words:\t").split(), key = len, reverse = True)
print("The longest word You type in is: '", line[0],"'. It has ", len(line[0]), "letters."  )


