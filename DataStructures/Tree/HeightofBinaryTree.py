class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
     
# return the Height of the given Binary Tree
def height(root):
    # code here
    if not root:
        return 0
    global x
    x = [1]
    def traverse(i,root):
        if root:
            if i>x[0]:
                x[0] = i
            if root.left:
                traverse(i+1,root.left)
            if root.right:
                traverse(i+1,root.right)
        return
    traverse(1,root)
    return(x[0])