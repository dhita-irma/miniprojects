import unittest
from datastructure.trie import Trie


def create_trie(words):
    mytrie = Trie()
    for word in words:
        mytrie.insert(word)
    return mytrie


class TestTrie(unittest.TestCase):

    def test_add_empty(self):
        mytrie = Trie()
        mytrie.insert("hello")
        self.assertTrue(mytrie.find("hello"))
        self.assertFalse(mytrie.find("hell"))

    def test_add_with_words(self):
        mytrie = Trie()
        mytrie.insert("hello")
        mytrie.insert("hi")
        mytrie.insert("world")
        mytrie.insert("worlds")
        self.assertTrue(mytrie.find("worlds"))

    def test_find_with_empty(self):
        mytrie = Trie()
        result = mytrie.find("hey")
        self.assertFalse(result)

    def test_find_with_words(self):
        mytrie = create_trie(["hello", "hi", "hey"])
        result = mytrie.find("hey")
        self.assertTrue(result)

    def test_find_does_not_exist(self):
        mytrie = create_trie(["hello", "hi", "hey"])
        result = mytrie.find("world")
        self.assertFalse(result)

    def test_delete_empty(self):
        mytrie = Trie()
        result = mytrie.delete("hello")
        self.assertFalse(result)

    def test_delete_with_one_word(self):
        mytrie = Trie()
        mytrie.insert("hello")
        result = mytrie.delete("hello")
        self.assertTrue(result)
        self.assertFalse(mytrie.find("hello"))

    def test_delete_with_many_words(self):
        mytrie = create_trie(["hello", "hi", "hey"])
        result = mytrie.delete("hey")
        self.assertTrue(result)
        self.assertFalse(mytrie.find("hey"))

    def test_delete_word_does_not_exist(self):
        mytrie = create_trie(["hello", "hi"])
        result = mytrie.delete("hey")
        self.assertFalse(result)
