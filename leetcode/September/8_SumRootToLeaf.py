class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.res = 0
        def traverse(root,s):
            if root:
                s += str(root.val)
                if not root.left and not root.right:
                    self.res += int(s,2)
                    return
                traverse(root.left,s)
                traverse(root.right,s)
            return
        traverse(root,'')
        return(self.res)