#! /usr/bin/python
# -*- coding: utf-8 -*-


def P(i, j):
    P = {(0, 0): 0.5}
    if i == j == 0:
        return P[(0, 0)]
    for x in range(i+1):
        for y in range(j+1):
            if x == y == 0:
                continue
            elif y == 0 and x > 0:
                P[(x, 0)] = 0.0

            elif x == 0 and y > 0:
                P[(0, y)] = 1.0

            else:
                P[(x, y)] = 0.5 * (P[(x-1, y)] + P[(x, y-1)])

    return P[(i, j)]


import unittest


class TestP(unittest.TestCase):
    def test_simple_P(self):
        self.assertEqual(P(0, 0), 0.5)
        self.assertEqual(P(1, 0), 0.0)
        self.assertEqual(P(0, 1), 1.0)

if __name__ == '__main__':
    unittest.main()
