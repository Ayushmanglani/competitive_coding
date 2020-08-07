from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        order = defaultdict(list)
        def traverse(root,level,h):
            if root:
                order[level].append((h,root.val))
                traverse(root.left,level-1,h+1)
                traverse(root.right,level+1,h+1)
                return
            return
        traverse(root,0,1)
        result = []
        order = sorted(order.items(), key = lambda i:i)
        
        for k, v in dict(order).items():
            v_sorted = sorted(v)
            tmp = []
            for _, n in v_sorted:
                tmp.append(n)
            result.append(tmp)
        
        return result