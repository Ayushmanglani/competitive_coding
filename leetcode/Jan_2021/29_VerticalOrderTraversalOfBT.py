class Solution(object):
    def verticalTraversal(self, root):
        def verticalTraversalUtil(root,hz,ht,myDict):
            queue = deque([(root,0,0)])
            while queue:
                node,dis,ht = queue.popleft()
                if node is not None:
                    myDict.append((dis,ht,node.val))
                    queue.append((node.left,dis-1,ht+1))
                    queue.append((node.right,dis+1,ht+1))
                    
        myDict = []
        verticalTraversalUtil(root,0,0,myDict)
        #print(myDict)
        myDict.sort()
        
        #print(myDict)
        res = OrderedDict()
        for item in myDict:
            if item[0] in res:
                res[item[0]].append(item[2])
            else:
                res[item[0]] = [item[2]]
        return res.values()