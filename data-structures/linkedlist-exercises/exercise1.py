#  Write a Python program to create a singly linked list,
#  append some items and iterate through the list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_item = Node(value)
        if not self.head:
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item

    def iterate(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


if __name__ == '__main__':

    list0 = LinkedList()
    list0.append('Python')
    list0.append('Java')
    list0.append('JavaScript')

    list0.iterate()