class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def postOrder_traversal(node, result):
    if node:
           
        postOrder_traversal(node.left, result)  
        postOrder_traversal(node.right, result)  
        result.append(node.value)  


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
# Perform preorder traversal
result = []
postOrder_traversal(root, result)
print("Postorder traversal:", result)
