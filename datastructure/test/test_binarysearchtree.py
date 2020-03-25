import unittest
from datastructure.binarysearchtree import BinarySearchTree


def create_binary_tree(items):
    bst = BinarySearchTree()
    for item in items:
        bst.insert(item)
    return bst


class TestBinarySearchTree(unittest.TestCase):

    def test_insert_empty(self):
        bst = BinarySearchTree()
        result = bst.insert(100)
        self.assertEqual(result, True)
        self.assertEqual(bst.root.value, 100)
        self.assertEqual(bst.count, 1)

    def test_insert_with_items(self):
        bst = BinarySearchTree()
        bst.insert(100)
        bst.insert(95)
        bst.insert(150)
        result = bst.insert(125)
        self.assertEqual(result, True)
        self.assertEqual(bst.count, 4)
        # TODO: test find 125

    def test_insert_item_duplicate(self):
        bst = BinarySearchTree()
        bst.insert(100)
        bst.insert(95)
        result = bst.insert(95)
        self.assertEqual(result, False)
        self.assertEqual(bst.root.value, 100)
        self.assertEqual(bst.count, 2)

    def test_find_exist(self):
        bst = create_binary_tree([100, 95, 150, 125])
        self.assertEqual(bst.find(95), True)

    def test_find_does_not_exist(self):
        bst = create_binary_tree([100, 95, 150, 125])
        self.assertEqual(bst.find(200), False)

    def test_delete_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.delete(100), None)

    # TREE FOR DELETE LEAF
    #                50
    #             /      \
    #            30      70
    #           /  \    /  \
    #          20  40  60   80

    def test_delete_leaf(self):
        bst = create_binary_tree([50, 30, 20, 40, 70, 60, 80])
        bst.delete(20)
        self.assertEqual(bst.count, 6)
        self.assertEqual(bst.root, 50)

    # TREE FOR DELETE NODE THAT HAS ONLY ONE CHILD
    #                50
    #             /      \
    #            30      70
    #              \    /  \
    #              40  60   80

    def test_delete_node_that_has_only_one_child(self):
        bst = create_binary_tree([50, 30, 40, 70, 60, 80])
        bst.delete(30)
        self.assertEqual(bst.count, 5)
        self.assertEqual(bst.root, 50)
        self.assertEqual(bst.find(40), True)

    # TREE FOR DELETE NODE THAT HAS TWO CHILDREN
    #                50
    #             /      \
    #            30      70
    #                   /  \
    #                  60   80

    def test_delete_node_that_has_two_children(self):
        bst = create_binary_tree([50, 40, 70, 60, 80])
        bst.delete(70)
        self.assertEqual(bst.count, 4)
        self.assertEqual(bst.root, 50)
        self.assertEqual(bst.find(40), True)

    def test_get_size_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.get_size(), 0)

    def test_get_size_with_items(self):
        bst = create_binary_tree([100, 95, 150, 125])
        self.assertEqual(bst.get_size(), 4)
