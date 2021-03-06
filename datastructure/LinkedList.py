class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value):
        """Append an element to the end of the list."""
        new_item = Node(value)
        if not self.head:           # If there is no element in the list
            self.head = new_item
            self.tail = new_item
        else:                       # If there are elements in the list
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1

    def pop(self):
        """Remove the last element of the list and return the value of the popped element."""

        # If there is no element in the list
        if not self.head:
            return None

        # If there is only 1 element in the list
        elif self.count == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.count = 0
            return value

        # If there are more than 1 element in the list
        else:
            current = self.head
            while current.next.next:  # Find second to last element
                current = current.next

            value = current.next.value
            current.next = None
            self.tail = current
            self.count -= 1
            return value

    def get_value(self, i):
        """Return element at the index i"""
        if i >= self.count or i < 0:
            raise IndexError

        current_item = self.head
        current_index = 0
        while current_index != i:
            current_item = current_item.next
            current_index += 1
        return current_item.value

    def insert(self, value, i):
        """Insert an element at index i"""
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
            current.next = new_item

        self.count += 1

    def remove_at_index(self, i):
        """Remove element at index i"""
        if i >= self.count or i < 0:
            raise IndexError

        if i == 0:
            self.head = self.head.next
            self.count -= 1
        elif i == self.count-1:
            self.pop()
        else:
            current_item = self.head
            current_index = 0
            while current_index != i - 1:
                current_item = current_item.next
                current_index += 1

            current_item.next = current_item.next.next
            self.count -= 1

    def remove_value(self, value):
        """Remove the first element that contains value"""
        if self.head.value == value:
            self.remove_at_index(0)
        elif self.tail.value == value:
            self.pop()
        else:
            current = self.head

            # Find the element before the element that contains said value
            while current and current.next.value != value:
                current = current.next

            current.next = current.next.next
            self.count -= 1

    def count(self):
        """Return the total element in the list."""
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
