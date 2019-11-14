#!/usr/bin/python
#-*- coding: utf-8 -*-
import unittest
from times import *

class TestTime(unittest.TestCase):
    def setUp(self):
        self.tenSeconds = Time(10)
        self.oneSecond = Time(1)
        self.oneMinute = Time(60)
        self.oneHour = Time(3600)
        self.halfHour = Time(1800)
        self.someTime  = Time(4785)


    def test_init(self):
        self.assertEqual(self.tenSeconds.s, 10)
        self.assertEqual(self.oneSecond.s, 1)
        self.assertEqual(self.oneMinute.s, 60)
        self.assertEqual(self.someTime.s, 4785)
        self.assertEqual(self.oneHour.s, 3600)

    def test_print(self):
        # test str()
        self.assertEqual(str(self.tenSeconds),"00:00:10")
        self.assertEqual(str(self.oneHour),"01:00:00")
        self.assertEqual(str(self.oneMinute),"00:01:00")
        self.assertEqual(str(self.someTime),"01:19:45")
        self.assertEqual(str(self.oneSecond),"00:00:01")

        # test repr()

        self.assertEqual(repr(self.tenSeconds),"Time(10)")
        self.assertEqual(repr(self.oneSecond),"Time(1)")
        self.assertEqual(repr(self.oneHour),"Time(3600)")
        self.assertEqual(repr(self.oneMinute),"Time(60)")
        self.assertEqual(repr(self.someTime),"Time(4785)")

        
    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(30) + Time(30), self.oneMinute)
        self.assertEqual(Time(0) + Time(1), self.oneSecond)
    
    def test_compare(self):
        self.assertTrue(Time(30) > Time(10))
        self.assertTrue(Time(15) < Time(20))
        self.assertTrue(Time(1) == Time(1))

    def test_int(self):
        self.assertEquals(int(self.oneSecond), 1)
        self.assertEquals(int(self.oneHour), 3600)
        self.assertEquals(int(self.oneMinute), 60)

if __name__ == "__main__":
    unittest.main()

