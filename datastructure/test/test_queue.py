import unittest
from datastructure.queue import Queue


def create_queue(items):
    myqueue = Queue()
    for item in items:
        myqueue.enqueue(item)
    return myqueue


class TestQueue(unittest.TestCase):

    def test_enqueue_with_items(self):
        myqueue = Queue()
        myqueue.enqueue('Python0')
        myqueue.enqueue('Python1')
        myqueue.enqueue('Python2')
        self.assertEqual(myqueue.get_size(), 3)
        self.assertEqual(myqueue.peek(), 'Python0')

    def test_enqueue_empty(self):
        myqueue = Queue()
        myqueue.enqueue('Python0')
        self.assertEqual(myqueue.get_size(), 1)
        self.assertEqual(myqueue.peek(), 'Python0')

    def test_dequeue_with_items(self):
        myqueue = create_queue(["Python0", "Python1", "Python2"])
        result = myqueue.dequeue()
        self.assertEqual(result, 'Python0')
        self.assertEqual(myqueue.get_size(), 2)
        self.assertEqual(myqueue.peek(), 'Python1')

    def test_dequeue_with_one_item(self):
        myqueue = create_queue(["Python0"])
        result = myqueue.dequeue()
        self.assertEqual(result, 'Python0')
        self.assertEqual(myqueue.get_size(), 0)
        self.assertEqual(myqueue.peek(), None)

    def test_dequeue_empty(self):
        myqueue = Queue()
        result = myqueue.dequeue()
        self.assertEqual(result, None)
        self.assertEqual(myqueue.get_size(), 0)
        self.assertEqual(myqueue.peek(), None)

    def test_peek_with_itmes(self):
        myqueue = create_queue(["Python0", "Python1", "Python2"])
        result = myqueue.peek()
        self.assertEqual(result, 'Python0')

    def test_peek_empty(self):
        myqueue = Queue()
        result = myqueue.peek()
        self.assertEqual(result, None)

    def test_get_size_with_items(self):
        myqueue = create_queue(["Python0", "Python1", "Python2"])
        self.assertEqual(myqueue.get_size(), 3)

    def test_get_size_empty(self):
        myqueue = Queue()
        self.assertEqual(myqueue.get_size(), 0)
