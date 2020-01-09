#!usr/bin/python
# -*- coding: utf-8 -*-
import unittest


class Queue:
    def __init__(self, size):
        self.n = size + 1
        self.size = size
        self.items = self.n * [None]
        self.head = 0
        self.tail = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise IndexError("Queue is full!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise IndexError("Queue is empty!")
        data = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.n
        return data


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(5)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())

    def test_put(self):
        self.queue.put(5)
        self.assertEqual(self.queue.head, 0)
        self.assertEqual(self.queue.items[self.queue.head], 5)

    def test_get(self):
        for x in range(self.queue.size):
            self.queue.put(x)

        for x in range(self.queue.size):
            self.assertEqual(self.queue.get(), x)

    def test_is_empty_2(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.put(42)
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        for x in range(self.queue.size):
            self.queue.put(x)

        self.assertTrue(self.queue.is_full())

    def test_put_with_full_queue(self):
        for x in range (self.queue.size):
            self.queue.put(x)

        self.assertRaises(IndexError, lambda: self.queue.put(42))

    def test_get_with_empty_queue(self):
        self.assertRaises(IndexError, lambda: self.queue.get())

    if __name__ == "__main__":
        unittest.main()
