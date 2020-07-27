class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        indexpost = [len(postorder)-1]
        def create(indexpost,inorder):
            if inorder:
                new = postorder[indexpost[0]]
                node = TreeNode(new)  
                indexpost[0] -= 1
                i = inorder.index(new)
                node.right = create(indexpost,inorder[i+1:])
                node.left = create(indexpost,inorder[:i])        
                return node 
            return
        return(create(indexpost,inorder))