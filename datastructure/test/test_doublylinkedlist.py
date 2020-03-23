import unittest
from datastructure.doublylinkedlist import DoublyLinkedList


def create_doubly_linked_list(items):
    mylist = DoublyLinkedList()
    for item in items:
        mylist.append(item)
    return mylist


class TestDoublyLinkedList(unittest.TestCase):

    def test_append_empty(self):
        mylist = DoublyLinkedList()
        mylist.append('Java')
        self.assertEqual(mylist.head.value, 'Java')
        self.assertEqual(mylist.count, 1)

    def test_append_with_items(self):
        mylist = DoublyLinkedList()
        mylist.append('Java')
        mylist.append('Ruby')
        mylist.append('Python')
        self.assertEqual(mylist.tail.value, 'Python')
        self.assertEqual(mylist.count, 3)

    def test_pop_empty(self):
        mylist = DoublyLinkedList()
        result = mylist.pop()
        self.assertEqual(mylist.count, 0)
        self.assertEqual(mylist.head, None)
        self.assertEqual(result, None)

    def test_pop_with_one_item(self):
        mylist = DoublyLinkedList()
        mylist.append('Java')
        result = mylist.pop()
        self.assertEqual(mylist.count, 0)
        self.assertEqual(mylist.head, None)
        self.assertEqual(result, 'Java')

    def test_pop_with_more_than_one_items(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'Python'])
        result = mylist.pop()
        self.assertEqual(mylist.count, 2)
        self.assertEqual(mylist.head.value, 'Java')
        self.assertEqual(result, 'Python')

    def test_get_value_i__bigger_than_count(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'Python'])

        with self.assertRaises(IndexError):
            mylist.get_value(3)

    def test_get_value_i_less_than_zero(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'Python'])

        with self.assertRaises(IndexError):
            mylist.get_value(-2)

    def test_get_value(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'Python'])
        result = mylist.get_value(1)
        self.assertEqual(result, 'Ruby')

    def test_insert_i_bigger_than_count(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'Python'])

        with self.assertRaises(IndexError):
            mylist.insert('C++', 4)

    def test_insert_i_less_than_zero(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'Python'])

        with self.assertRaises(IndexError):
            mylist.insert('C++', -1)

    def test_insert_at_tail(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'C++'])
        mylist.insert('Python', 3)
        self.assertEqual(mylist.tail.value, 'Python')
        self.assertEqual(mylist.count, 4)

    def test_insert_at_head(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'C++'])
        mylist.insert('Python', 0)
        self.assertEqual(mylist.tail.value, 'C++')
        self.assertEqual(mylist.head.value, 'Python')
        self.assertEqual(mylist.count, 4)

    def test_insert(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'C++'])
        mylist.insert('Python', 2)
        self.assertEqual(mylist.tail.value, 'C++')
        self.assertEqual(mylist.count, 4)
        self.assertEqual(mylist.get_value(2), 'Python')

    def test_remove_at_index_bigger_than_count(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'Python'])

        with self.assertRaises(IndexError):
            mylist.remove_at_index(3)

    def test_remove_at_index_less_than_zero(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'Python'])

        with self.assertRaises(IndexError):
            mylist.remove_at_index(-1)

    def test_remove_index_zero(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'Python'])
        mylist.remove_at_index(0)
        self.assertEqual(mylist.head.value, 'Ruby')
        self.assertEqual(mylist.count, 2)

    def test_remove_index_last(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'Python'])
        mylist.remove_at_index(2)
        self.assertEqual(mylist.tail.value, 'Ruby')
        self.assertEqual(mylist.count, 2)

    def test_remove_index(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.remove_at_index(1)
        self.assertEqual(mylist.tail.value, 'JavaScript')
        self.assertEqual(mylist.count, 2)

    def test_remove_value_head(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.remove_value('Java')
        self.assertEqual(mylist.head.value, 'Ruby')
        self.assertEqual(mylist.count, 2)

    def test_remove_value_tail(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.remove_value('JavaScript')
        self.assertEqual(mylist.tail.value, 'Ruby')
        self.assertEqual(mylist.count, 2)

    def test_remove_value(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.remove_value('Ruby')
        self.assertEqual(mylist.tail.value, 'JavaScript')
        self.assertEqual(mylist.count, 2)

    def test_count(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'JavaScript'])
        self.assertEqual(mylist.count, 3)

    def test_find_empty(self):
        mylist = DoublyLinkedList()
        self.assertEqual(mylist.find('Python'), None)

    def test_find_item_not_in_the_list(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'JavaScript'])
        self.assertEqual(mylist.find('Python'), None)

    def test_find_item_in_the_list(self):
        mylist = create_doubly_linked_list(['Java', 'Ruby', 'JavaScript'])
        self.assertEqual(mylist.find('Ruby'), 1)

