class Solution(object):
    def pseudoPalindromicPaths (self, root):
        def dfs(root, count=0):
            if not root: return 0
            count ^= 1 << (root.val - 1)
            res = dfs(root.left, count) + dfs(root.right, count)
            if root.left == root.right:
                if count & (count - 1) == 0:
                    res += 1
            return res
        return dfs(root)

class Solution(object):
    def pseudoPalindromicPaths (self, root):
        self.count = 0
        def search(node, digitcount):
            digitcount = digitcount ^ (1 << node.val)
            if node.left:
                search(node.left, digitcount)
            
            if node.right:
                search(node.right, digitcount)
                
            if not node.left and not node.right:
                if digitcount & (digitcount - 1) == 0:
                    self.count += 1
                return
        search(root, 0)
        return self.count        