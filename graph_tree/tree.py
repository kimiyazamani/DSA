class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)

        return root

    def _get_min_value(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def remove(self, key):
        self.root = self._remove_recursive(self.root, key)

    def _remove_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._remove_recursive(root.left, key)
        elif key > root.key:
            root.right = self._remove_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.key = self._get_min_value(root.right)
            root.right = self._remove_recursive(root.right, root.key)

        return root