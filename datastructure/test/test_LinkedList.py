import unittest
from datastructure.LinkedList import LinkedList


def create_linked_list(items):
    mylist = LinkedList()
    for item in items:
        mylist.append(item)
    return mylist


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
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        result = mylist.pop()
        self.assertEqual(mylist.count, 2)
        self.assertEqual(mylist.head.value, 'Java')
        self.assertEqual(result, 'JavaScript')

    def test_get_value_i__bigger_than_count(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])

        with self.assertRaises(IndexError):
            mylist.get_value(3)

    def test_get_value_i_less_than_zero(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])

        with self.assertRaises(IndexError):
            mylist.get_value(-2)

    def test_get_value(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        result = mylist.get_value(1)
        self.assertEqual(result, 'Ruby')

    def test_insert_i_bigger_than_count(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])

        with self.assertRaises(IndexError):
            mylist.insert('Python', 4)

    def test_insert_i_less_than_zero(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])

        with self.assertRaises(IndexError):
            mylist.insert('Python', -1)

    def test_insert_at_tail(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.insert('Python', 3)
        self.assertEqual(mylist.tail.value, 'Python')
        self.assertEqual(mylist.count, 4)

    def test_insert_at_head(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.insert('Python', 0)
        self.assertEqual(mylist.tail.value, 'JavaScript')
        self.assertEqual(mylist.head.value, 'Python')
        self.assertEqual(mylist.count, 4)

    def test_insert(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.insert('Python', 2)
        self.assertEqual(mylist.tail.value, 'JavaScript')
        self.assertEqual(mylist.count, 4)
        self.assertEqual(mylist.get_value(2), 'Python')

    def test_remove_at_index_bigger_than_count(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])

        with self.assertRaises(IndexError):
            mylist.remove_at_index(3)

    def test_remove_at_index_less_than_zero(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])

        with self.assertRaises(IndexError):
            mylist.remove_at_index(-1)

    def test_remove_index_zero(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.remove_at_index(0)
        self.assertEqual(mylist.head.value, 'Ruby')
        self.assertEqual(mylist.count, 2)

    def test_remove_index_last(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.remove_at_index(2)
        self.assertEqual(mylist.tail.value, 'Ruby')
        self.assertEqual(mylist.count, 2)

    def test_remove_index(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.remove_at_index(1)
        self.assertEqual(mylist.tail.value, 'JavaScript')
        self.assertEqual(mylist.count, 2)

    def test_remove_value_head(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.remove_value('Java')
        self.assertEqual(mylist.head.value, 'Ruby')
        self.assertEqual(mylist.count, 2)

    def test_remove_value_tail(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.remove_value('JavaScript')
        self.assertEqual(mylist.tail.value, 'Ruby')
        self.assertEqual(mylist.count, 2)

    def test_remove_value(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        mylist.remove_value('Ruby')
        self.assertEqual(mylist.tail.value, 'JavaScript')
        self.assertEqual(mylist.count, 2)

    def test_count(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        self.assertEqual(mylist.count, 3)

    def test_find_empty(self):
        mylist = LinkedList()
        self.assertEqual(mylist.find('Python'), None)

    def test_find_item_not_in_the_list(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        self.assertEqual(mylist.find('Python'), None)

    def test_find_item_in_the_list(self):
        mylist = create_linked_list(['Java', 'Ruby', 'JavaScript'])
        self.assertEqual(mylist.find('Ruby'), 1)

