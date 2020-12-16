class Solution(object):
    def isValidBST(self, root):
        
        def check_bst(node, left, right):
            if not node:
                return True

            if not left < node.val < right:
                return False

            return (check_bst(node.left, left, node.val) and check_bst(node.right, node.val, right))
        
        return check_bst(root, float("-inf"), float("inf"))