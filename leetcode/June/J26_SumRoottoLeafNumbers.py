class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root:
            res = 0
            def traverse(root,temp):
                if root is None:
                    return
                temp = temp*10 + root.val
                if root.left is None and root.right is None: 
                    nonlocal res
                    res += temp
                else:
                    traverse(root.left,temp)
                    traverse(root.right,temp)
            traverse(root,0)
            return(res)
        return(0)

'''Method2 -->
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        stack = [(0,root)]
        
        if not root: return 0
        ans = 0 
        while stack:
            n,root = stack.pop()

            if root: n = n*10 + root.val
            if not root.left and not root.right:
                ans += n
            
            if root.right: stack.append((n,root.right))
            if root.left: stack.append((n,root.left))
        
        return ans