class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.total = 0

    def add(self, value):
        """ Add to the end of the list """
        new_element = Node(value)
        if not self.head:
            self.head = new_element
        else:
            current = self.head
            while current.next:  # while my current has a next Node
                current = current.next
            # add the element to the last node in the list
            current.next = new_element

        self.total += 1  # update total

    def pop(self):
        """ Remove the end of the list """
        if not self.head:
            return None

        # if there is only one element
        if self.total == 1:
            value = self.head.value
            self.head = None  # removing the only element in the list
            self.total = 0
            return value

            # loop through and find last element
        current = self.head
        while current.next.next:  # find second to last element
            current = current.next

        value = current.next.value
        current.next = None
        self.total -= 1
        return value

    def get_at_index(self, i):
        """ return element at index i """
        if i >= self.total or i < 0:
            raise IndexError

        current_index = 0
        current = self.head
        while current_index != i:
            current = current.next
            current_index += 1

        return current.value

    def insert_at_index(self, i, value):
        """ insert an element at a certain index i """

        if i > self.total or i < 0:
            raise IndexError

        if i == self.total:
            self.add(value)
            return

        current_index = 0
        current = self.head
        while current_index != i - 1:  # make current is element before i
            current = current.next
            current_index += 1

        # current = element at index i - 1
        # current.next = element at index i (we are going to move it to i + 1)
        new_node = Node(value)
        new_node.next = current.next  # what ever is at index i now will be i + 1
        current.next = new_node  # make i-1.next  = new node
        self.total += 1

    def remove_at_index(self, i):
        """ remove an element at index i """
        if i >= self.total or i < 0:
            raise IndexError

        if i == self.total:
            self.pop()
            return

        current_index = 0
        current = self.head
        while current_index != i - 1:  # make current is element before i
            current = current.next
            current_index += 1

        node_at_i_plus_1 = current.next.next  # element at i + 1
        current.next = node_at_i_plus_1
        self.total -= 1

    def count(self):
        """ get total number of elements inside the list """
        return self.total

    def find(self, value):
        """ return the index of the first element that contains the value,
            or None is doesnt exist
        """

        if self.total == 0:
            return None

        i = 0
        current = self.head
        while current and current.value != value:
            current = current.next
            i += 1

        return i if current else None
