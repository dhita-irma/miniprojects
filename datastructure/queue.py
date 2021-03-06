from datastructure.doublylinkedlist import DoublyLinkedList


class Queue:

    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the value of an item at the front of the queue"""
        if self.queue.count > 0:
            value = self.peek()
            self.queue.remove_at_index(0)
            return value
        else:
            return None

    def peek(self):
        """Return value of the item at the front of the list without removing it"""
        if self.queue.count > 0:
            return self.queue.head.value
        else:
            return None

    def get_size(self):
        return self.queue.count
