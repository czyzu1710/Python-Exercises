#!/usr/bin/python
#-*- coding: utf-8 -*-

RN = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
NotNextToEachOther =set(['L', 'D', 'V'])
def roman2arabic(RomanNum):
    wasSmallerBefore= False
    result = []
    for x in RomanNum:
        if  x not in RN:
            print("Not a roman number! Possible digits are: 'I', 'V', 'X', 'L', 'C','D','M'.")
            return -1

    for x in range(len(RomanNum)):
        result.append(RN[RomanNum[x]])
        if x > 0:
            if RomanNum[x] == RomanNum[x-1]:
                if RomanNum[x] in NotNextToEachOther:
                    print("Wrong sequence!")
                    return -3
            if RN[RomanNum[x-1]] < RN[RomanNum[x]]:
                    result.append(RN[RomanNum[x]] - (RN[RomanNum[x-1]]*2))
                    result.append(-RN[RomanNum[x]])
        if x>1:
            if RN[RomanNum[x-2]] < RN[RomanNum[x]]:
                print("Wrong sequence!")
                return -2
        if x>=3:
            if RomanNum[x-3] == RomanNum[x]:
                print("Wrong sequence! Max three similar digits")
                return -3
            
    print(sum(result))

roman2arabic("XIX")

