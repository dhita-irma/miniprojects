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
        self.assertTrue(result)
        self.assertTrue(bst.find(100))
        self.assertTrue(bst.is_valid())
        self.assertEqual(bst.root.value, 100)
        self.assertEqual(bst.count, 1)

    def test_insert_with_items(self):
        bst = BinarySearchTree()
        bst.insert(100)
        bst.insert(95)
        bst.insert(150)
        result = bst.insert(125)
        self.assertTrue(result)
        self.assertTrue(bst.find(125))
        self.assertEqual(bst.count, 4)
        self.assertTrue(bst.is_valid())

    def test_insert_item_duplicate(self):
        bst = BinarySearchTree()
        bst.insert(100)
        bst.insert(95)
        result = bst.insert(95)
        self.assertFalse(result)
        self.assertEqual(bst.root.value, 100)
        self.assertEqual(bst.count, 2)
        self.assertTrue(bst.is_valid())

    def test_find_empty(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.find(95))

    def test_find_one_item(self):
        bst = create_binary_tree([100])
        self.assertTrue(bst.find(100))

    def test_find_exist(self):
        bst = create_binary_tree([100, 95, 150, 125])
        self.assertTrue(bst.find(95))

    def test_find_does_not_exist(self):
        bst = create_binary_tree([100, 95, 150, 125])
        self.assertFalse(bst.find(200))

    def test_preorder(self):
        bst = create_binary_tree([50, 30, 20, 40, 70, 60, 80])
        result = bst.preorder()
        self.assertEqual(result, [50, 30, 20, 40, 70, 60, 80])

    def test_inorder(self):
        bst = create_binary_tree([50, 30, 20, 40, 70, 60, 80])
        result = bst.inorder()
        self.assertEqual(result, [20, 30, 40, 50, 60, 70, 80])

    def test_postorder(self):
        bst = create_binary_tree([50, 30, 20, 40, 70, 60, 80])
        result = bst.postorder()
        self.assertEqual(result, [20, 40, 30, 60, 80, 70, 50])

    def test_delete_empty(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.delete(100))
        self.assertTrue(bst.is_valid())

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
        self.assertFalse(bst.find(20))
        self.assertTrue(bst.is_valid())

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
        self.assertFalse(bst.find(30))
        self.assertTrue(bst.find(40))
        self.assertTrue(bst.is_valid())

    # TREE FOR DELETE NODE THAT HAS TWO CHILDREN
    #                50
    #              /     \
    #             40     70
    #                   /  \
    #                  60   80

    def test_delete_node_that_has_two_children(self):
        bst = create_binary_tree([50, 40, 70, 60, 80])
        bst.delete(70)
        self.assertEqual(bst.count, 4)
        self.assertFalse(bst.find(70))
        self.assertTrue(bst.find(60))
        self.assertTrue(bst.find(80))
        self.assertTrue(bst.is_valid())

    def test_delete_node_that_is_a_root(self):
        bst = create_binary_tree([50, 30, 20, 40, 70, 60, 80])
        bst.delete(50)
        self.assertEqual(bst.count, 6)
        self.assertEqual(bst.root.value, 60)
        self.assertFalse(bst.find(50))
        self.assertTrue(bst.find(30))
        self.assertTrue(bst.find(80))
        self.assertTrue(bst.is_valid())

    def test_get_size_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.get_size(), 0)

    def test_get_size_with_items(self):
        bst = create_binary_tree([100, 95, 150, 125])
        self.assertEqual(bst.get_size(), 4)

    def test_is_valid_empty(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_valid())

    def test_is_valid_with_items(self):
        bst = create_binary_tree([50, 30, 20, 40, 70, 60, 80])
        self.assertTrue(bst.is_valid())

    def test_min_value(self):
        bst = create_binary_tree([50, 30, 20, 40, 70, 60, 80])
        result = bst.min_value()
        self.assertTrue(result, 20)

    def test_min_value_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.min_value(), None)

    def test_max_value(self):
        bst = create_binary_tree([50, 30, 20, 40, 70, 60, 80])
        result = bst.max_value()
        self.assertTrue(result, 80)

    def test_max_value_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.max_value(), None)
