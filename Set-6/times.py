#!usr/bin/python
#-*- coding: utf-8 -*-

class Time: 
    def __init__(self, seconds = 0):
        self.s = int (seconds)

    def __str__(self):
        h = int(self.s / 3600)
        sec  = self.s - h * 3600
        m = int(sec/60)
        sec = int(sec - m * 60)
        return "{0:02d}:{1:02d}:{2:02d}".format(h,m,sec)
    
    def __repr__(self):
        return "Time({0})".format(self.s)

    def __add__(self, other):
        return Time(self.s + other.s)

    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.s > other.s

    def __lt__(self, other):
        return self.s < other.s

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def __int__(self):
        return self.s

