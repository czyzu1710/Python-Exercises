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
        self.assertEqual(add_frac(self.half, self.oneThird),[5,6])
        self.assertEqual(add_frac(self.half, self.half), [1,1])
        self.assertEqual(add_frac(self.half, self.oneQuarter),[3,4])
        self.assertEqual(add_frac(self.oneQuarter, self.oneThird), [7,12])
    
    
    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.half, self.oneQuarter),[1,4])
        self.assertEqual(sub_frac([3,4],[1,4]),[1,2])
        self.assertEqual(sub_frac(self.half, self.minOneQuarter),[3,4])
    
    
    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.half,self.half),[1,4])
        self.assertEqual(mul_frac(self.half,self.oneQuarter), [1,8])
        self.assertEqual(mul_frac(self.oneThird, self.half),[1,6])
   

    def test_div_frac(self):
        self.assertEqual(div_frac(self.half,self.half),[1,1])
        self.assertEqual(div_frac(self.half,self.oneQuarter), [2,1])
        self.assertEqual(div_frac(self.oneThird, self.half),[2,3])
    

    def test_isPositive(self):
        self.assertTrue(isPositive(self.half))
        self.assertFalse(isPositive(self.minhalf))

    def test_isZero(self):
        self.assertTrue(isZero(self.zero))
        self.assertFalse(isZero(self.oneQuarter))
    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.half, [1,2]),0)
        self.assertEqual(cmp_frac(self.half, self.threeQuarters),-1)
        self.assertEqual(cmp_frac([3,4], self.half),1)
if __name__ == '__main__':
    unittest.main()
