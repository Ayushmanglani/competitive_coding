# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def level(root, a, l):
    if root is None:
        return 0
    if root.val == a:
        return l

    lv = level(root.left,a,l+1)
    if lv != 0:
        return lv
    return level(root.right,a,l+1)
    
def isSibling(root,a,b):
    
    if root is None: 
        return 0
    
    try:
        if (root.left.val == a and root.right.val == b) or (root.left.val == b and root.right.val == a) :
            return True
    except:
        if (root.left == a and root.right == b) or (root.left == b and root.right == a) :
            return True
    return (isSibling(root.left, a, b) or isSibling(root.right, a, b))
    
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if ((level(root,x,1) == level(root, y, 1)) and 
            not (isSibling(root, x, y))): 
            return 1
        else: 
            return 0 
    