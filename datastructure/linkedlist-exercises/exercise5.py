# Write a Python program to set a new value of an item in a singly linked list using index value.
# Write a Python program to delete the first item from a singly linked list.
# Write a Python program to delete the last item from a singly linked list.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value):
        """Add an item to the end of the list."""
        new_item = Node(value)
        if not self.head:
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1

    def iterate(self):
        """Print all of the elements in the list"""
        current = self.head
        while current:
            value = current.value
            current = current.next
            yield value

    def find(self, value):
        """Find an element that contains value, return True if value exists and
            return False if value doesn't not exist."""
        current = self.head
        while current.value.lower() != value.lower() and current.next:
            current = current.next
        return current.value.lower() == value.lower()

    def value_at_index(self, i):
        """Find the element on index i and return the value"""
        if i >= self.count or i < 0:
            raise IndexError

        current = self.head
        current_index = 0
        while current_index != i:
            current = current.next
            current_index += 1
        return current.value

    def set_value_at_index(self, value, i):
        """Set a new value of an element located at index i"""
        if i >= self.count or i < 0:
            raise IndexError

        new_item = Node(value)
        current = self.head
        current_index = 0

        while current_index != i-1:
            current = current.next
            current_index += 1

        new_item.next = current.next.next
        current.next = new_item

    def pop_head(self):
        """Delete the first item of a list"""
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count = 0
        else:
            self.head = self.head.next
            self.count -= 1

    def pop_tail(self):
        """Delete the last item of a list"""
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count = 0
        else:
            current = self.head
            current_index = 0
            while current_index != self.count-2:
                current = current.next
                current_index += 1

            self.tail = current
            current.next = None
            self.count -= 1


if __name__ == '__main__':

    list0 = LinkedList()
    list0.append('Python')          # 0
    list0.append('Java')            # 1
    list0.append('JavaScript')      # 2
    list0.append('C')               # 3
    list0.append('C++')             # 4

    list0.pop_tail()

    for value in list0.iterate():
        print(value)
