class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

def LeftView(root):
    x = []
    i = 0
    def view(i,root):
        if root:
            # print(x)
            if i not in x:
                x.append(i)
                print(root.data, end=" ")
            if root.left:
                view(i+1,root.left)
            if root.right:
                view(i+1,root.right)
    view(i,root)

