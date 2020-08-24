class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.x = 0
        def traverse(root):      
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                self.x += root.left.val
            traverse(root.left)
            traverse(root.right)        
        traverse(root)
        return(self.x)