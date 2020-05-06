import unittest
from datastructure.stack import Stack


def create_stack(items):
    mystack = Stack()
    for item in items:
        mystack.push(item)
    return mystack


class TestStack(unittest.TestCase):

    def test_push(self):
        mystack = Stack()
        mystack.push('Python0')
        self.assertEqual(mystack.count(), 1)
        self.assertEqual(mystack.peek(), 'Python0')

    def test_pop_empty(self):
        mystack = Stack()
        result = mystack.pop()
        self.assertEqual(result, None)

    def test_pop_with_one_item(self):
        mystack = create_stack(['Python0'])
        result = mystack.pop()
        self.assertEqual(result, 'Python0')
        self.assertEqual(mystack.count(), 0)

    def test_pop_with_more_than_one_items(self):
        mystack = create_stack(['Python0', 'Python1', 'Python2', 'Python3'])
        result = mystack.pop()
        self.assertEqual(result, 'Python3')
        self.assertEqual(mystack.count(), 3)
        self.assertEqual(mystack.peek(), 'Python2')

    def test_peek_empty(self):
        mystack = Stack()
        result = mystack.peek()
        self.assertEqual(result, None)
        self.assertEqual(mystack.count(), 0)

    def test_peek_with_items(self):
        mystack = create_stack(['Python0', 'Python1', 'Python2', 'Python3'])
        result = mystack.peek()
        self.assertEqual(result, 'Python3')
        self.assertEqual(mystack.count(), 4)

    def test_clear_empty(self):
        mystack = Stack()
        result = mystack.clear()
        self.assertEqual(result, None)

    def test_clear_with_items(self):
        mystack = create_stack(['Python0', 'Python1', 'Python2', 'Python3'])
        mystack.clear()
        self.assertEqual(mystack.count(), 0)
        self.assertEqual(mystack.peek(), None)

    def test_is_empty_with_empty(self):
        mystack = Stack()
        self.assertTrue(mystack.is_empty())

    def test_is_empty_with_items(self):
        mystack = create_stack(['Python0'])
        result = mystack.is_empty()
        self.assertEqual(result, False)
