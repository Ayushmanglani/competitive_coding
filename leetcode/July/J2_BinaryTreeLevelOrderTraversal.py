from collections import defaultdict
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        l = 0
        level = defaultdict(list)            
        def traverse(root,l):
            if not root:
                return
            level[l].append(root.val)
            traverse(root.left,l+1)
            traverse(root.right,l+1)            
        traverse(root,l)
        level = sorted(level.values(), key = lambda i: level.keys())
        return(level[::-1])