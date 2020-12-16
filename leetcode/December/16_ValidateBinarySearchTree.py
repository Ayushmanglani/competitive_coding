class Solution(object):
    def isValidBST(self, root):
        
        def check_bst(node, left, right):
            if not node:
                return True

            if not left < node.val < right:
                return False

            return (check_bst(node.left, left, node.val) and check_bst(node.right, node.val, right))
        
        return check_bst(root, float("-inf"), float("inf"))

class Solution(object):
    def isValidBST(self, root):
    
        stack, inorder = [], float("-inf")      
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
            
        return True        