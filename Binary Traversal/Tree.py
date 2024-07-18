class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = TreeNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = TreeNode(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.value)
            self._inorder_traversal(root.right, result)
        return result
    
    def print_tree(self, node, level=0, label='.'):
        indent = ' ' * (4 * level)
        print(f"{indent}{label}: {node.value if node else 'None'}")
        if node:
            if node.left or node.right:
                self.print_tree(node.left, level + 1, 'L')
                self.print_tree(node.right, level + 1, 'R')
    #Delete
   
        

# Usage
bst = BinarySearchTree()
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    bst.insert(key)
    print(f"After inserting {key}:")
    bst.print_tree(bst.root)
    print("\n")

# Inorder traversal
print("Inorder traversal of the BST:")
print(bst.inorder_traversal())

# Search for a value
key = 90
result = bst.search(key)
if result is not None:
    print(f"Key {key} found in the BST.")
else:
    print(f"Key {key} not found in the BST.")
