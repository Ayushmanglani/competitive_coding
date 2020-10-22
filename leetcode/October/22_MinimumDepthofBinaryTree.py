class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        self.depth = 99999
        def dfs(root,l):
            if not root:
                return
            if not root.left and not root.right:
                if l<self.depth:    
                    self.depth = l
            dfs(root.left,l+1)
            dfs(root.right,l+1)
        dfs(root,1)
        return self.depth