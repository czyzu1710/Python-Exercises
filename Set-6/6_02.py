#!/usr/bin/python
#-*- coding: utf-8 -*-
import unittest
from points import *

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.zero = Point(0, 0)
        self.oneZero = Point(1, 0)
        self.zeroOne = Point(0, 1)
        self.twoOne = Point(2,1)
        self.oneTwo = Point(1,2)

    def test_init(self):
        self.assertEqual([self.zero.x, self.zero.y], [0, 0])
        self.assertEqual([self.oneZero.x, self.oneZero.y], [1,0])
        self.assertEqual([self.zeroOne.x, self.zeroOne.y], [0,1])
        self.assertEqual([self.oneTwo.x, self.oneTwo.y], [1,2])

    def test_print(self):
        #test str()
        self.assertEqual(str(self.zero), "(0, 0)")
        self.assertEqual(str(self.oneZero), "(1, 0)")
        self.assertEqual(str(self.oneTwo), "(1, 2)")

        #test repr()
        self.assertEqual(repr(self.zero), "Point(0, 0)")
        self.assertEqual(repr(self.oneZero), "Point(1, 0)")
        self.assertEqual(repr(self.oneTwo), "Point(1, 2)")

    def test_add(self):
        self.assertEqual(Point(1, 1) + Point(1, 1), Point(2, 2))
        self.assertEqual(Point(2, 1) + self.zero, Point(2, 1))
        self.assertEqual(Point(2, 2) + Point(-2, -2), Point(0, 0))
    
    def test_sub(self):
        self.assertEqual(Point(1, 1) - Point(1, 1), Point(0, 0))
        self.assertEqual(Point(1, 3) - Point(1, 2), Point(0, 1))
        self.assertEqual(Point(0, 0) - Point(1, 1), Point(-1, -1))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(2, 3), 8)
        self.assertEqual(Point(2, 2) * Point(2, 2), 8)
        self.assertEqual(Point(3, 7) * Point(4, 5), 47)
    
    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(1, 2)), 0)
        self.assertEqual(Point(2, 1).cross(Point(3, 2)), 1)
        self.assertEqual(Point(3, 7).cross(Point(5,6)), -17)

    def test_length(self):
        self.assertEqual(self.zero.length(), 0)
        self.assertEqual(self.oneTwo.length(), 5**(1/2))
        self.assertEqual(Point(2**(1/2),2**(1/2)).length(), 2)
if __name__ == "__main__":
    unittest.main()

