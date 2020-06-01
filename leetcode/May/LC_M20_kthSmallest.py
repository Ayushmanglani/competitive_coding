# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inarr = []
        def inorder(root):
            if len(inarr) >= k:
                return
            if root:
                inorder(root.left) 
                inarr.append((root.val))
                inorder(root.right)
        i = inorder(root)
        return(inarr[k-1])