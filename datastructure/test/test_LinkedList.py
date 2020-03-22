import unittest
from datastructure.LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_append_empty(self):
        mylist = LinkedList()
        mylist.append('Java')
        self.assertEqual(mylist.head.value, 'Java')
        self.assertEqual(mylist.count, 1)

    def test_append_with_items(self):
        mylist = LinkedList()
        mylist.append('Java')
        mylist.append('Ruby')
        mylist.append('JavaScript')
        self.assertEqual(mylist.tail.value, 'JavaScript')
        self.assertEqual(mylist.count, 3)

    def test_pop_empty(self):
        mylist = LinkedList()
        result = mylist.pop()
        self.assertEqual(mylist.count, 0)
        self.assertEqual(mylist.head, None)
        self.assertEqual(result, None)

    def test_pop_with_one_item(self):
        mylist = LinkedList()
        mylist.append('Java')
        result = mylist.pop()
        self.assertEqual(mylist.count, 0)
        self.assertEqual(mylist.head, None)
        self.assertEqual(result, 'Java')

    def test_pop_with_more_than_one_items(self):
        mylist = LinkedList()
        mylist.append('Java')
        mylist.append('Ruby')
        mylist.append('JavaScript')
        result = mylist.pop()
        self.assertEqual(mylist.count, 2)
        self.assertEqual(mylist.head.value, 'Java')
        self.assertEqual(result, 'JavaScript')

    def test_get_value_i__bigger_than_count(self):
        mylist = LinkedList()
        mylist.append('Java')
        mylist.append('Ruby')

        with self.assertRaises(IndexError):
            mylist.get_value(2)

    def test_get_value_i_less_than_zero(self):
        mylist = LinkedList()
        mylist.append('Java')
        mylist.append('Ruby')

        with self.assertRaises(IndexError):
            mylist.get_value(-2)

    def test_get_value(self):
        mylist = LinkedList()
        mylist.append('Java')
        mylist.append('Ruby')
        result = mylist.get_value(1)
        self.assertEqual(result, 'Ruby')

