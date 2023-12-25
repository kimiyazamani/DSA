class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def create_node(self, key):
        return Node(key)

    def min_value(self, root):
        while root.left:
            root = root.left
        return root.key

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return self.create_node(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self.min_value(root.right)
            root.right = self._remove(root.right, root.key)
        
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root is not None
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def pre_order_traversal(self, root):
        if root is not None:
            print(root.key, end=' ')
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def in_order_traversal(self, root):
        if root is not None:
            self.in_order_traversal(root.left)
            print(root.key, end=' ')
            self.in_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root is not None:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.key, end=' ')