#!usr/bin/python
#-*- coding: utf-8 -*-
import fractions

def add_frac(frac_1, frac_2):
    result = [0,0] 
    if frac_1[1] != frac_2[1]:
        frac_1[0] *= frac_2[1]
        frac_2[0] *= frac_1[1]
        frac_1[1]  = frac_2[1] = frac_1[1] * frac_2[1]
        
        result[0] = frac_1[0] + frac_2[0]
        result[1] = frac_1[1]
        gcd  = fractions.gcd(result[0], result[1])
        return [result[0]/gcd, result[1]/gcd]


def sub_frac(frac_1, frac_2):
    frac_2[0] = -frac_2[0]
    return add_frac(frac_1, frac_2)


def mul_frac(frac_1, frac_2):
    result = [0,0]
    result[0] = frac_1[0] * frac_2[0]
    result[1] = frac_1[1] * frac_2[1]
    gcd = fractions.gcd(result[0],result[1])
    return [result[0]/gcd, result[1]/gcd]

def div_frac(frac_1, frac_2):
    return mul_frac(frac_1, frac_2.reverse())


def isPositive(frac_1):
    return frac_[0] > 0 and frac_1[1] > 0


def isZero(frac_1):
    return frac_1[0] == 0

def cmp_frac(frac_1, frac_2):
    frac = sub_frac(frac_1, frac_2)
    if frac[0] == 0:
        return 0
    elif (frac[0] < 0 and frac[1] > 0) or (frac[0] > 0 and frac[1] < 0):
        return -1
    else:
        return 1

def frac2float(frac):
    return frac[0]/frac[1]


