import unittest


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SingleList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        result = "List["
        node = self.head
        while node is not None:
            result += str(node)
            if not node == self.tail:
                result += ", "
            node = node.next
        result += "]"
        return result

    def is_empty(self):
        return self.length == 0

    def count(self):
        return self.length

    def insert_head(self, node):
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):
        if self.is_empty():
            raise IndexError("The list is empty!")
        node = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None
        self.length -= 1
        return node

    def search(self, data):
        node = self.head
        while node is not None and node.data != data:
            node = node.next
        return node

    def find_max(self):
        maximum = node = self.head
        while node is not None:
            if node.data > maximum.data:
                maximum = node
            node = node.next
        return maximum

    def find_min(self):
        minimum = node = self.head
        while node is not None:
            if node.data < minimum.data:
                minimum = node
            node = node.next
        return minimum

    def reverse(self):
        if self.length > 1:
            current = self.head.next
            parent = self.head
            self.tail = parent
            parent.next = None
            while current is not None:
                tmp = current.next
                current.next = parent
                parent = current
                current = tmp
            self.head = parent


class TestSingleList(unittest.TestCase):
    def setUp(self):
        self.list = SingleList()

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())

    def test_insert_tail(self):
        self.list.insert_tail(Node(1))
        self.assertEqual(self.list.head.data, Node(1).data)

    def test_insert_head(self):
        self.list.insert_tail(Node(1))
        self.list.insert_head(Node(2))
        self.assertEqual(self.list.tail.data, Node(1).data)
        self.assertEqual(self.list.head.data, Node(2).data)

    def test_str(self):
        for x in range(5):
            self.list.insert_tail(Node(x))
        self.assertEqual(str(self.list), "List[0, 1, 2, 3, 4]")

    def test_count(self):
        for x in range(10):
            self.list.insert_tail(Node(x))
        self.assertEqual(self.list.count(), 10)

    def test_is_empty2(self):
        self.list.insert_tail(Node(1))
        self.assertFalse(self.list.is_empty())

    def test_remove_head(self):
        self.list.insert_tail(Node(42))
        self.assertEqual(self.list.remove_head().data, Node(42).data)

    def test_search(self):
        for x in range(10):
            self.list.insert_tail(Node(x))
        self.assertEqual(self.list.search(5).data, Node(5).data)
        self.assertIsNone(self.list.search(10))
        node = self.list.search(5)

    def test_find_max(self):
        for x in range(10):
            self.list.insert_tail(Node(x))
        self.assertEqual(self.list.find_max().data, Node(9).data)
        print(self.list)
        self.list.search(5).data = 10
        print(self.list)
        self.assertEqual(self.list.find_max().data, Node(10).data)

    def test_find_min(self):
        for x in range(10):
            self.list.insert_tail(Node(x))
        self.assertEqual(self.list.find_min().data, Node(0).data)
        print(self.list)
        self.list.search(5).data = -5
        self.assertEqual(self.list.find_min().data, Node(-5).data)
        print(self.list)

    def test_reverse(self):
        for x in range(10):
            self.list.insert_tail(Node(x))
        print(self.list)
        self.list.reverse()
        print(self.list)


if __name__ == '__main__':
    unittest.main()
