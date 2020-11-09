class Solution(object):
    def maxAncestorDiff(self, root):
        self.diff = 0            
        def traverse(root,minst,maxst):
            if root:
                minst = min(minst,root.val)
                maxst = max(maxst,root.val)
                self.diff = max(self.diff,abs(minst-maxst))
                traverse(root.left,minst,maxst)
                traverse(root.right,minst,maxst)
        traverse(root,root.val,root.val)
        return self.diff 