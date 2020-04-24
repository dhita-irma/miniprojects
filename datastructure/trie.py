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

        if not self.root:
            return False

        # If trie is not empty
        # Put the nodes in a stack
        current = self.root
        node_stack = Stack()
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
            node_stack.push(current)

        if not current.is_end:
            return False

        # Delete node from the end of key if node does not have children
        current.is_end = False
        for i in range(node_stack.count()):
            current = node_stack.pop()
            prev = node_stack.peek()
            if not current.children and prev:
                del prev.children[current.char]
        return True

    def contains_prefix(self, prefix):
        """Returns True as long as the prefix exist in the Trie"""
        if not self.root:
            return False

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def __get_all_words(self, current, path_so_far, word_list):
        """
        Get all words from current node and all of its children.
        :param current: current node in the Trie
        :param path_so_far: the string that represent some characters from root up to but not including current node
        :param word_list: total words that will be return at the end
        """

        # Check if current node is valid (not null)
        # Add the current nodes character to the end of path so far
        # If current node is the end of a word
        #     Add path_so_far to the word_list
        # For each child
        #     Call get_all_words on each child
        # Return word_list

        if not current:
            return False

        path_so_far += current.char

        if current.is_end:
            word_list.append(path_so_far)

        for child in current.children.values():
            self.__get_all_words(child, path_so_far, word_list)

        return word_list

    def get_words_with_prefix(self, prefix):
        """"Returns  a list of words in the Trie that starts with the prefix"""

        # Traverse the path to get to the last character node
        # Set "current" to be the last character node
        # Traverse on each child of "current" until reaching the end of the word
        # Get all words

        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return self.__get_all_words(current, prefix[:-1], [])
