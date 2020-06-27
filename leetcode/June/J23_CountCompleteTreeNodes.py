class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root:
            h = [0]
            def traverse(root):
                if root: 
                    h[0] += 1
                    traverse(root.left)
                    traverse(root.right)
                return
            traverse(root)
            return(h[0])
        return(0)
'''
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ld = self.get_depth(root.left)
        rd = self.get_depth(root.right)
        if ld == rd:
            return 2 ** ld + self.countNodes(root.right)
        return 2 ** rd + self.countNodes(root.left)

    def get_depth(self, node):
        if node is None:
            return 0
        return 1 + self.get_depth(node.left)