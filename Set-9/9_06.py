import unittest
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def count_leafs(top: Node):
    result = 0
    if top is None:
        return 0
    if top.left is None and top.right is None:
        result += 1
    result += count_leafs(top.left)
    result += count_leafs(top.right)
    return result


def count_total(top: Node):
    result = 0
    if top is None:
        return 0
    result += top.data
    result += count_total(top.left)
    result += count_total(top.right)
    return result


class TestTree(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)

    def test_count_leafs(self):
        self.assertEqual(count_leafs(self.root), 4)
        self.root.left.left.left = Node(8)
        self.root.left.left.right = Node(9)
        self.assertEqual(count_leafs(self.root), 5)

    def test_count_total(self):
        self.assertEqual(count_total(self.root), 28)
        self.root.left.left.left = Node(8)
        self.root.left.left.right = Node(9)
        self.assertEqual(count_total(self.root), 45)


if __name__ == "__main__":
    unittest.main()
