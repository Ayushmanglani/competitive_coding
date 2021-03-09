#addOneRow
class Solution(object):
    def addOneRow(self, root, v, d):        
        if d == 1:
            new = TreeNode(v)
            new.left = root
            return new
        
        self.d = d
        self.v = v
        def traverse(root,l):
            if root:
                if self.d == l+1:
                    new1 = TreeNode(self.v)
                    new2 = TreeNode(self.v)
                    new1.left = root.left
                    new2.right = root.right
                    root.left = new1
                    root.right = new2
                    return
                traverse(root.left,l+1)
                traverse(root.right,l+1)
        
        traverse(root,1)
        return root