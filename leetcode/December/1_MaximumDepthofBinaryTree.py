#Maximum Depth of Binary Tree
class Solution(object):
    def maxDepth(self, root):
        self.depth = 0
        if not root:
            return 0
        def traverse(root,d):
            if root:
                if d>self.depth:
                    self.depth = d
                traverse(root.left,d+1)
                traverse(root.right,d+1)
            return
        traverse(root,1)
        return self.depth