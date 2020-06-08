class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# return True if the given tree is a BST, else return False
def isBST(root):
    if root and not root.left and not root.right:
        return True
    x = []
    def inorder(root):
        if root:
            if root.left:
                inorder(root.left)
            x.append(root.data)
            if root.right:
                inorder(root.right)
    inorder(root)
    y = x.copy()
    y.sort()

    if x == y and len(set(x)) > 1:
        return True
    return False
