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

    def __delete(self):
        pass

    def delete(self, value):
        """Delete a node containing value in a tree"""
        if self.root:
            deletion = self.delete(value)
            if deletion:
                self.count -= 1
            return deletion
        else:
            return None

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
