class Solution(object):
    def rob(self, root):
        def helper(node):            
            if not node:
                # Base case:
                # empty node
                # Both not to take and take are zero
                return (0, 0)
                
            # General case:
            # profit tuple of left sub-tree
            left = helper(node.left)
            # profit tuple of right sub-tree
            right = helper(node.right)

            # If current node is not taken, then optimal = max profit of left sub-tree + max profit of right sub-tree
            not_to_take_cur = max(left) + max(right)

            # If current node is taken, then optimal = max profit of not to take child node + current node value
            take_cur = left[0] + right[0] + node.val
            
            return (not_to_take_cur, take_cur)
        return max(helper(node=root))