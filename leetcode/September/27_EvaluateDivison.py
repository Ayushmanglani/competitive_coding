from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append([equations[i][1],values[i]])
            graph[equations[i][1]].append([equations[i][0],(1/values[i])])
        
        output_list = []
        def dfs(curr_node,dst,val,visited):
            if(curr_node in visited or curr_node not in graph):
                return False
            visited.add(curr_node)
            if(curr_node==dst):
                output_list.append(val)
                return True
            for node in graph[curr_node]:
                if(dfs(node[0],dst,val*node[1],visited)):
                    return True
            
            return False
        for query in queries:
            src = query[0]
            dst = query[1]
            visited = set()
            if(not dfs(src,dst,1,visited)):
                output_list.append(-1)
        return output_list