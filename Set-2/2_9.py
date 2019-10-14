#!/usr/bin/python
#-*- coding: utf-8
afile = open('2_9_output.txt','w+')
with open('2_9_input.txt','r') as f:
    for line in f:
        if line[0]== '#':
            continue
        
        else:
            afile.write(line)

    
