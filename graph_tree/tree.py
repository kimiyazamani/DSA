class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insert_recursive(self.root, key)

    def insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self.insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self.insert_recursive(root.right, key)

        return root

    def get_min_value(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def remove(self, key):
        self.root = self.remove_recursive(self.root, key)

    def remove_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.remove_recursive(root.left, key)
        elif key > root.key:
            root.right = self.remove_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.key = self.get_min_value(root.right)
            root.right = self.remove_recursive(root.right, root.key)

        return root