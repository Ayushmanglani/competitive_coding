from collections import defaultdict
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        level = defaultdict(list)
        def traverse(root,l):
            if root:
                level[l].append(root.val)
                traverse(root.left,l+1)
                traverse(root.right,l+1)
        traverse(root,0)
        res = []
        for i in level:
            if i%2 == 0:
                res.append(level[i])
            else:
                res.append(level[i][::-1])
        return res        