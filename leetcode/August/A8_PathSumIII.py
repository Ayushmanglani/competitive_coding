class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.total = 0
        def traverse(root,start,s):
            if not root: return
            s -= root.val
            if s == 0:
                self.total += 1
            traverse(root.left,False,s)
            traverse(root.right,False,s)
            if start == True:
                traverse(root.left,True,sum) #Traverse with left child as Root
                traverse(root.right,True,sum)
                
        traverse(root,True,sum)
        return(self.total)