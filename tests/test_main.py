import unittest

from main import Node
from main import Stack


class TestNode(unittest.TestCase):
    n1 = Node(5, None)
    n2 = Node('a', n1)

    def test_attributes(self):
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, 'a')
        self.assertEqual(self.n1, self.n1)
        self.assertEqual(self.n2.next_node, self.n1)


class TestStack(unittest.TestCase):
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')

    def test_push(self):
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            Node(self.stack.top.next_node.next_node.next_node.data)
