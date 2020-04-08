class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.count = 0

    def __insert(self, current_node, value):
        if value == current_node.value:
            return False  # Cannot insert duplicate
        elif value < current_node.value:
            if current_node.left:
                return self.__insert(current_node.left, value)
            else:
                current_node.left = Node(value)
        else:
            if current_node.right:
                return self.__insert(current_node.right, value)
            else:
                current_node.right = Node(value)
        return True

    def insert(self, value):
        """Add a node to a BST. Return True if value inserted,
            otherwise, return False"""
        if self.root:
            insertion = self.__insert(self.root, value)
            if insertion:
                self.count += 1
            return insertion
        else:
            self.root = Node(value)
            self.count += 1
            return True

    def __find(self, current_node, value):
        if value == current_node.value:
            return True
        elif value < current_node.value:
            if current_node.left:
                return self.__find(current_node.left, value)
        else:
            if current_node.right:
                return self.__find(current_node.right, value)
        return False

    def find(self, value):
        """Find a value in the tree, return True if value exist.
           Otherwise, return False."""
        if self.root:
            return self.__find(self.root, value)
        else:
            return False

    def __delete(self, current_node, value):
        """Returns a a new subtree in which the node of 'value' is deleted.
            Current_node may or may not change, depend on which node is deleted"""
        if not current_node:  # If current_node is None
            return current_node
        if current_node.value == value:
            if not current_node.right:  # Current_node has only left child or no child
                return current_node.left
            elif not current_node.left:  # Current_node has only right child or no child
                return current_node.right
            else:  # current_node has two children
                successor = self.__inorder_successor(current_node)
                current_node.value = successor.value
                current_node.right = self.__delete(current_node.right, current_node.value)
        elif value < current_node.value:
            current_node.left = self.__delete(current_node.left, value)
        else:  # Value > current_node.value
            current_node.right = self.__delete(current_node.right, value)
        return current_node

    def __inorder_successor(self, current_node):
        """Return a new node in a subtree that is greater than current_node (root) and
            smaller than everything else"""
        current_node = current_node.right
        while current_node.left:
            current_node = current_node.left
        return current_node

    def delete(self, value):
        """Delete a node containing value in a tree"""
        if self.root and self.find(value):
            self.__delete(self.root, value)
            self.count -= 1
            return True
        return False

    def __preorder(self, current_node, item_list):
        item_list.append(current_node.value)
        if current_node.left:
            self.__preorder(current_node.left, item_list)
        if current_node.right:
            self.__preorder(current_node.right, item_list)
        return item_list

    def preorder(self):
        """Traverse Root - Left - Right"""
        if self.root:
            return self.__preorder(self.root, [])
        else:
            return []

    def __postorder(self, current_node, item_list):
        if current_node.left:
            self.__postorder(current_node.left, item_list)
        if current_node.right:
            self.__postorder(current_node.right, item_list)
        item_list.append(current_node.value)
        return item_list

    def postorder(self):
        """Traverse Left - Right - Root"""
        if self.root:
            return self.__postorder(self.root, [])
        else:
            return []

    def __inorder(self, current_node, item_list):
        if current_node.left:
            self.__inorder(current_node.left, item_list)
        item_list.append(current_node.value)
        if current_node.right:
            self.__inorder(current_node.right, item_list)
        return item_list

    def inorder(self):
        """Traverse Left - Root - Right"""
        if self.root:
            return self.__inorder(self.root, [])
        else:
            return []

    def get_size(self):
        return self.count

    def __isvalid(self, current_node):
        if not current_node:  # This is the base case
            return True
        elif current_node.left and current_node.value <= current_node.left.value:  # check if this is not a valid node
            return False
        elif current_node.right and current_node.value >= current_node.right.value:  # check if this is not a valid node
            return False
        return self.__isvalid(current_node.left) and self.__isvalid(current_node.right)  # This is the recursive case

    def is_valid(self):
        if self.root:
            return self.__isvalid(self.root)
        else:
            return True

    def min_value(self):
        if self.root:
            current_node = self.root
            if current_node.left:
                current_node = current_node.left
            return current_node.value
        else:
            return None

    def max_value(self):
        if self.root:
            current_node = self.root
            if current_node.right:
                current_node = current_node.right
            return current_node.value
        else:
            return None
