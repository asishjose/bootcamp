
class Node:
    def __init__(self,val):
        self.key = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(6)
root.left.right = Node(4)

def inorder(root):
    if root is None:
        return root
    inorder(root.left)
    print(root.key)
    inorder(root.right)

def height(root):
    if root is None:
        return 0
    return 1+max(height(root.left),height(root.right))

print(height(root))