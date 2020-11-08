class Solution(object):
    def findTilt(self, root):
        self.total = 0
        def addtraverse(root):
            if not root:
                return 0

            l = r = 0
            if root.left:
                l = addtraverse(root.left)
            if root.right:
                r = addtraverse(root.right)

            self.total += abs(l-r)
            return l + r + root.val
        addtraverse(root)
        return(self.total)
        