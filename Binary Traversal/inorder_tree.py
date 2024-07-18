class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def inOrder_traversal(node, result):
    if node:
           
        inOrder_traversal(node.left, result)  
        result.append(node.value)  
        inOrder_traversal(node.right, result)   


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
# Perform preorder traversal
result = []
inOrder_traversal(root, result)
print("Inorder traversal:", result)
