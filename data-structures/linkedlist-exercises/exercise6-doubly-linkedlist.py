# Write a Python program to create a doubly linked list, append some items and iterate through the list (print forward)


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value):
        """Add an item to the end of the list"""
        new_item = Node(value)
        if self.count == 0:
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            new_item.prev = self.tail
            self.tail = new_item
        self.count += 1

    def iterate(self):
        current = self.head
        while current:
            val = current.value
            current = current.next
            yield val


if __name__ == '__main__':

    list1 = DLinkedList()
    list1.append('Python')      # 0
    list1.append('Java')        # 1
    list1.append('JavaScript')  # 2
    list1.append('C')           # 3
    list1.append('C++')         # 4

    for value in list1.iterate():
        print(value)
