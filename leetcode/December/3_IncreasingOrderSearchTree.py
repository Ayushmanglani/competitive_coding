# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        stack = []
        if not root or not root.left and not root.right:
            return root
        # Taking left subtree in Stack
        def traverse(root):
            if root:
                traverse(root.right)
                stack.append(root.val)
                traverse(root.left)
            return
        if root.left:
            traverse(root.left)
        
        new = None
        #Making tree from stack
        if stack:
            new = TreeNode(stack.pop())
        cur = new
        while stack:
            cur.right = TreeNode(stack.pop())
            cur = cur.right
            
        # Adding root node to stack
        if cur:
            cur.right = TreeNode(root.val)
            cur = cur.right
        else:
            new = TreeNode(root.val)
            cur = new
            
        # Making right subtree in Stack
        def traverse(root):
            if root:
                traverse(root.left)
                stack.append(root.val)
                traverse(root.right)
            return
        if root.right:
            traverse(root.right)
        
        # Adding root node to stack 
        while stack:
            cur.right = TreeNode(stack.pop(0))
            cur = cur.right
        return new

class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right        