#!usr/bin/pytohn
#-*- coding: utf-8 -*-
import unittest
from fracs import *

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0,1]
        self.half = [1,2]
        self.minhalf = [-1,2]
        self.oneThird = [1,3]
        self.minOneThird = [1, -3]
        self.threeQuarters = [3,4]
        self.minThreeQuarters = [-3,4]
        self.oneQuarter = [1,4]
        self.minOneQuarter = [1,-4]
    

    def test_add_frac(self):
        self.assertEquals(add_frac( self.half, self.oneThird),[5,6])


if __name__ == '__main__':
    unittest.main()
