class Solution(object):
    def rangeSumBST(self, root, low, high):
        self.total = 0
        def traverse(root):
            if root:
                if low<=root.val<=high:
                    self.total += root.val
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return self.total