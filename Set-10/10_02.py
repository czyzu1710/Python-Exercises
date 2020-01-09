#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest


class Stack:
    def __init__(self, size):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise IndexError("Stack is full")
        self.items[self.n] = data
        self.n -= -1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None
        return data


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(10)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())

    def test_push(self):
        self.stack.push(10)
        self.assertEqual(self.stack.items[0], 10)
        self.stack.push(20)
        self.assertEqual(self.stack.items[1], 20)
        self.assertEqual(self.stack.n, 2)

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.n, 1)

    def test_is_full2(self):
        self.assertFalse(self.stack.is_full())
        for x in range(self.stack.size):
            self.stack.push(x)

        self.assertTrue(self.stack.is_full())

    def test_pop_with_empty_stack(self):
        self.assertRaises(IndexError, lambda: self.stack.pop())

    def test_push_with_full_stack(self):
        for x in range(self.stack.size):
            self.stack.push(x)

        self.assertRaises(IndexError, lambda: self.stack.push(101))


if __name__ == "__main__":
    unittest.main()
