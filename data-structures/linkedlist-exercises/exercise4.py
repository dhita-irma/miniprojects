# Write a Python program to access a specific item in a singly linked list using index value.


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
            print(current.value)
            current = current.next
        print(f"Linked list size = {str(self.count)}")

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


if __name__ == '__main__':

    list0 = LinkedList()
    list0.append('Python')          # 0
    list0.append('Java')            # 1
    list0.append('JavaScript')      # 2
    list0.append('C')               # 3

    print(list0.value_at_index(2)
