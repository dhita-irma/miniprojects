# Write a Python program to create a doubly linked list, append some items and iterate through the list (print forward)
# Print nodes from current position to first
# count the number of items of a given doubly linked list
# print a given doubly linked list in reverse order
# insert an item in front of a given doubly linked list


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


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
        """Iterate through a list"""
        current = self.head
        while current:
            val = current.value
            current = current.next
            yield val

    def reverse_order(self):
        """Print value from the current position to the first"""
        current = self.tail
        while current:
            val = current.value
            current = current.prev
            yield val

    def count(self):
        return self.count


if __name__ == '__main__':

    list1 = DLinkedList()
    list1.append('Python')      # 0
    list1.append('Java')        # 1
    list1.append('JavaScript')  # 2
    list1.append('C')           # 3
    list1.append('C++')         # 4

    for value in list1.reverse_order():
        print(value)
