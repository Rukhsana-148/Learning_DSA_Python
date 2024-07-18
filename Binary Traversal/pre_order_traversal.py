class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def preorder_traversal(node, result):
    if node:
        result.append(node.value)         # Visit the root node
        preorder_traversal(node.left, result)    # Traverse left subtree
        preorder_traversal(node.right, result)   # Traverse right subtree


# Creating the tree
root = TreeNode(10)
root.left = TreeNode(9)
root.right = TreeNode(11)
root.left.left = TreeNode(7)
root.left.right = TreeNode(8)

# Perform preorder traversal
result = []
preorder_traversal(root, result)
print("Preorder traversal:", result)
