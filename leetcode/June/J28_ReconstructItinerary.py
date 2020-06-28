from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        graph = defaultdict(list)
        for i,j in tickets:
            graph[i].append(j)
        for key in graph: 
            graph[key] = sorted(graph[key], reverse=True)
        
        def traverse(airport):
            while graph[airport]:
                candidate = graph[airport].pop()
                traverse(candidate)
            res.append(airport)
        traverse("JFK")
        return(res[::-1])
