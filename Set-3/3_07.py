#!/usr/bin/python
#-*- coding: utf-8 -*-

def commonPart(sequenceA,sequenceB):
    result = []
    bresult=list(sequenceA)
    for x in sequenceA:
        for y in sequenceB:
            bresult.append(y)
            if x == y:
                result.append(x)
            
    print("(a) ",set(result))
    print("(b) ",set(bresult))


commonPart([1,1,2,2,4,7,8,3],[1,3,1,2,9,54])


