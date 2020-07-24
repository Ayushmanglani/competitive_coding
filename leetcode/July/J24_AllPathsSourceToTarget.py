class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        res = []
        def traverse(path,node):
            if node == target:
                res.append(path)
                return
            for i in graph[node]:
                traverse(path+[i],i)     
        for i in graph[0]:
            traverse([0,i],i)
        return(res)

#Method 2
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        res = []
        def traverse(path,node):
            path += "."+str(node)
            if node == target:
                actpath = path.split('.')
                res.append(actpath)
                return
            for i in graph[node]:
                traverse(path,i)     
        for i in graph[0]:
            traverse(str(0),i)
        return(res)