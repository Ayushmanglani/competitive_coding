class Solution(object):
    def subtreeWithAllDeepest(self, root):
        def deep(root):
            if not root: 
                return 0, None
            l, r = deep(root.left), deep(root.right)
            print(l[0],r[0])
            if l[0] > r[0]: 
                return l[0] + 1, l[1]
            elif l[0] < r[0]: 
                return r[0] + 1, r[1]
            else: 
                return l[0] + 1, root
        return deep(root)[1]
        
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        # Tag each node with it's depth.
        depth = {None: -1}
        def dfs(node, parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        max_depth = max(depth.itervalues())

        def answer(node):
            # Return the answer for the subtree at node.
            if not node or depth.get(node, None) == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R

        return answer(root)        