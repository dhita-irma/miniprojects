# Write a Python program to search a specific item in a singly linked list and
# return true if the item is found otherwise return false


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


if __name__ == '__main__':

    list0 = LinkedList()
    list0.append('Python')
    list0.append('Java')
    list0.append('JavaScript')
    list0.append('C')

    lang = input("Enter a programming language: ")
    if list0.find(lang):
        print(f"{lang} is in the list")
    else:
        print(f"{lang} is not in the list")
