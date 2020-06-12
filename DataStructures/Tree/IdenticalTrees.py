class Node:
    def _init_(self, data):
        self.right = None
        self.data = data
        self.left = None
# your task is to complete this function
# function should return true/false or 1/0

def isIdentical(root1, root2):
    global x
    x = []
    if root1 == root2:
        return True
    if root1 and root2:
        if(root1.data != root2.data):
            x.append(0)
    else:
        return False
    def Traverse(root1,root2):
        if root1 and root2 and len(x)<1:
            if (root1.data != root2.data):
                x.append(0)
            if (root1.left and not root2.left) or (root2.left and not root1.left):
                x.append(0)
            else:
                Traverse(root1.left,root2.left)
                
            if (root1.right and not root2.right) or (root2.right and not root1.right):
                x.append(0)
            else:
                Traverse(root1.right,root2.right)
            # x.append(1)
        # x.append(0)
    Traverse(root1,root2)
    # print(x)
    if 0 in x:
        return False
    return True
