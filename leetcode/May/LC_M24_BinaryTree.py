class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = preorder.copy()
        inorder.sort()
        def tree(ino,preorder):
            if len(ino) == 0:
                return None
            root = TreeNode(preorder[0])
            if len(ino) == 1:
                preorder.pop(0)
                return root
            i = ino.index(preorder[0])
            preorder.pop(0)
            root.left = tree(ino[:i],preorder)
            root.right = tree(ino[i+1:],preorder)
            return root       
        return(tree(inorder,preorder))