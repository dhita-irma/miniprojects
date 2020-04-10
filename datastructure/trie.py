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

    def __delete(self, current, word):
        pass

    def delete(self, word):
        if self.root and self.find(word):
            return self.__delete(self.root, word)
        return None
