class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and val:
            if root.val == val:
                return(root)
            elif root.val < val:
                return(self.searchBST(root.right,val))
            elif root.val > val:
                return(self.searchBST(root.left,val))
            else:
                return(None)              
        return