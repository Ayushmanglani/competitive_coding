class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        def traverse(root):
            if root:
                res.append(root.val)
                traverse(root.left)
                traverse(root.right)
            return
        traverse(root1)
        traverse(root2)
        res.sort()
        return res