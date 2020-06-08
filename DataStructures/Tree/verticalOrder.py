
def getVerticalOrder(root, hd, m): 
  
    if root is None: 
        return
      
    try: 
        m[hd].append(root.key) 
    except: 
        m[hd] = [root.key] 
      
    getVerticalOrder(root.left, hd-1, m) 
    getVerticalOrder(root.right, hd+1, m) 
  
def printVerticalOrder(root): 
      
    m = dict() 
    hd = 0 
    getVerticalOrder(root, hd, m) 
    for index, value in enumerate(sorted(m)): 
        for i in m[value]: 
            print(i, end=" ") 


#-------------------------------------------
'''
import collections
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

def verticalOrder(root): 
  
    if root is None: 
        return
    queue = [] 
    m = {} 
  
    hd_node = {} 
  
    queue.append(root) 
    hd_node[root] = 0
  
    m[0] = [root.data] 
  
    while len(queue) > 0: 
  
       temp = queue.pop(0) 
  
        if temp.left: 
            queue.append(temp.left) 
  
            hd_node[temp.left] = hd_node[temp] - 1
            hd = hd_node[temp.left] 
  
            if m.get(hd) is None: 
                m[hd] = [] 
  
            m[hd].append(temp.left.data) 
  
        if temp.right: 
            # Enqueue right child 
            queue.append(temp.right) 
  
            # store the horizontal distance of right child 
            # hd(right child) = hd(parent) + 1 
            hd_node[temp.right] = hd_node[temp] + 1
            hd = hd_node[temp.right] 
  
            if m.get(hd) is None: 
                m[hd] = [] 
  
            m[hd].append(temp.right.data) 
  
    # Sort the map according to horizontal distance 
    sorted_m = collections.OrderedDict(sorted(m.items())) 
  
    # Traverse the sorted map and print nodes at each horizontal distance 
    for i in sorted_m.values(): 
        for j in i: 
            print(j, end=" ") 

------------------------------------------------------------------------
def verticalOrder(root): 
    if root:
        x = []
        x.append([0,root.data])
        def traverse(i,root):
            if root:
                if root.left:
                    x.append([i-1,root.left.data])
                if root.right:
                    x.append([i+1,root.right.data])
                if root.left:
                    traverse(i-1,root.left)
                if root.right:
                    traverse(i+1,root.right)
            return
        traverse(0,root)
        x = sorted(x, key = lambda i: i[0])
        for i in x:
            print(i[1], end=" ")
    return
'''

