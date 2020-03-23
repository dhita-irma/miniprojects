class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
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

    def pop(self):
        """Remove and return the value of the last item of the list"""
        if self.count > 1:
            value = self.tail.value
            self.tail = self.tail.prev
            self.count -= 1
            return value
        elif self.count == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.count = 0
            return value
        else:
            return None

    def get_value(self, i):
        """Return element at the index i"""
        if i >= self.count or i < 0:
            raise IndexError

        current = self.head
        current_index = 0
        while current_index != i:
            current = current.next
            current_index += 1
        return current.value

    def insert(self, value, i):
        """Insert an item at index i"""
        if i > self.count or i < 0:
            raise IndexError

        new_item = Node(value)
        if i == self.count:
            self.tail.next = new_item
            self.tail = new_item
        elif i == 0:
            new_item.next = self.head
            self.head = new_item
        else:
            current = self.head
            current_index = 0
            while current_index != i - 1:
                current = current.next
                current_index += 1

            new_item.next = current.next
            current.next.prev = new_item
            current.next = new_item
            new_item.prev = current

        self.count += 1

    def remove_at_index(self, i):
        """Remove item at index i"""
        if i >= self.count or i < 0:
            raise IndexError

        if i == 0:
            self.head = self.head.next
            self.count -= 1
        elif i == self.count-1:
            self.pop()
        else:
            current = self.head
            current_index = 0
            while current_index != i:
                current = current.next
                current_index += 1

            current.prev.next = current.next
            current.next.prev = current.prev
            self.count -= 1

    def remove_value(self, value):
        """Delete a specific item from a list"""
        if self.head.value == value:
            self.remove_at_index(0)
        elif self.tail.value == value:
            self.pop()
        else:
            current = self.head
            while current and current.value != value:
                current = current.next

            current.prev.next = current.next
            current.next.prev = current.prev
            self.count -= 1

    def count(self):
        """Return the total items in the list."""
        return self.count

    def find(self, value):
        """Return the index of the first element that contains value
            Return None if element doesn't exist."""
        if self.count == 0:
            return None

        current_item = self.head
        current_index = 0
        while current_item and current_item.value != value:
            current_item = current_item.next
            current_index += 1

        return current_index if current_item else None
