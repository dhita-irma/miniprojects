from datastructure.stack import Stack


class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = Node('*')

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]
        current.is_end = True

    def find(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        if current.is_end:
            return True
        else:
            return False

    def delete(self, word):
        # If tree is empty
        if not self.root:
            return None

        # If trie is not empty
        # Put the nodes in a stack
        current = self.root
        node_stack = Stack()
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
            node_stack.push(current)

        # Delete node from the end of key if node does not have children
        if current.is_end:
            current.is_end = False
            for i in range(node_stack.count()):
                current = node_stack.pop()
                prev = node_stack.peek()
                if not current.children and prev:
                    del prev.children[current.char]
            return True
        else:
            return False
