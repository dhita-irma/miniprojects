class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if value == self.value:
            return False
        elif value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Node(value)
                return True
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)
                return True

    def find(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left:
                return self.left.find(value)
            else:
                return False
        else:
            if self.right:
                return self.right.find(value)
            else:
                return False

    def delete(self, value):
        if self.find(value):
            pass  # TODO
        else:
            return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.value))
            if self.right:
                self.right.inorder()


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, value):
        """Add a node to a BST. Return True if value inserted,
            otherwise, return False"""
        if self.root:
            insertion = self.root.insert(value)
            if insertion:
                self.count += 1
            return insertion
        else:
            self.root = Node(value)
            self.count += 1
            return True

    def find(self, value):
        """Find a value in the tree, return True if value exist.
           Otherwise, return False."""
        if self.root:
            return self.root.find(value)
        else:
            return False

    def delete(self, value):
        """Delete a node containing value in a tree"""
        if self.root:
            deletion = self.delete(value)
            if deletion:
                self.count -= 1
            return deletion
        else:
            return None

    def preorder(self):
        print('PreOrder')
        self.root.preorder()

    def postorder(self):
        print('PostOrder')
        self.root.postorder()

    def inorder(self):
        print('InOrder')
        self.root.inorder()

    def get_size(self):
        return self.count
