class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.total = 0

    def add(self, value):
        """Add an element to the end of the list."""
        new_item = Node(value)
        if not self.head:           # If there is no element in the list
            self.head = new_item
            self.tail = new_item
        else:                       # If there are elements in the list
            self.tail.next = new_item
            self.tail = new_item
        self.total += 1

    def pop(self):
        """Remove the last element of the list and return the value of the popped element."""
        if not self.head:
            return None

        # If there is only one element
        if self.total == 1:
            self.head = None # Removing the only element in the list
            self.total = 0

        # Loop through and find the last element
        current_item = self.head
        while current_item.next.next:          #Find second to last element
            current_item = current_item.next

        value = current_item.value
        current_item.next = None
        self.total -= 1
        return value

    def get_value(self, i):
        """Return element at the index i"""
        if i >= self.total or i < 0:
            raise IndexError

        current_item = self.head
        current_index = 0
        while current_index != i:
            current_item = current_item.next
            current_index += 1
        return current_item.value

    def insert(self, i, value):
        """Insert an element at index i"""
        if i > self.total or i < 0:
            raise IndexError

        current_item = self.head
        current_index = 0
        while current_index != i - 1:
            current_item = current_item.next
            current_index += 1

        new_item = Node(value)
        new_item.next = current_item.next
        current_item.next = new_item
        self.total += 1

    def remove_at_index(self, i):
        """Remove element at index i"""
        if i >= self.total or i < 0:
            raise IndexError

        current_item = self.head
        current_index = 0
        while current_index != i - 1:
            current_item = current_item.next
            current_index += 1

        current_item.next = current_item.next.next
        self.total -= 1

    def remove_value(self, value):
        """Remove the first element that contains value"""
        current_item = self.head
        while current_item.next.value != value:  # Find the element before the element that contains said value
            current_item = current_item.next

        current_item.next = current_item.next.next
        self.total -= 1

    def count(self):
        """Return the total element in the list."""
        return self.total

    def find(self, value):
        """Return the index of the first element that contains value
            Return None if element doesn't exist."""
        if self.total == 0
            return None

        current_item = self.head
        current_index = 0
        while current_item and current_item.value != value:
            current_item = current_item.next
            current_index += 1

        return current_index if current_item else None
