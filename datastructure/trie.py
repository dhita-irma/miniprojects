class Trie:

    def __init__(self):
        self.head = {}

    def insert(self, word):
        current = self.head

        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['*'] = True

    def find(self, word):
        current = self.head

        for char in word:
            if char not in current:
                return False
            current = current[char]
        if '*' in current:
            return True
        else:
            return False

    def delete(self, word):
        pass
