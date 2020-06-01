# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        def find(root):
            if not root:
                return
            if root and not root.left and not root.right:
                return root
            else:
                root.right, root.left = root.left, root.right
                find(root.left)
                find(root.right)
            return root
        return(find(root))