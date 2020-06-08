class Node:
    def init(self, val):
        self.right = None
        self.data = val
        self.left = None

# your task is to complete this function
# function should print the level order traversal of the binary tree in spiral order
# Note: You aren't required to print a new line after every test case
def printSpiral(root):
    if root:
        Q = dict()
        Q[0] = [root.data]
        def bfs(i,root):
            if root is None:
                return
            if root.left:
                try:
                    Q[i].append(root.left.data)
                except:
                    Q[i] = [root.left.data]
            if root.right:
                try:
                    Q[i].append(root.right.data)
                except:
                    Q[i] = [root.right.data]
            if root.left: 
                bfs(i+1,root.left)
            if root.right:
                bfs(i+1,root.right)
        bfs(1,root)    
        for i in Q:
            if i%2 == 0:
                for j in Q[i][::-1]:
                    print(j,end= " ")
            else:
                for j in Q[i]:
                    print(j,end= " ")
    return