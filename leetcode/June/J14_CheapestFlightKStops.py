class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, c in flights:
            graph[u].append((v, c))
           
        queue = collections.deque([(src, 0, 0)])
        minCost = float('inf')
        while queue:
            node, stops, costSoFar = queue.popleft()
            if node == dst:
                minCost = min(minCost, costSoFar)
                continue
               
            if stops > K or costSoFar > minCost:
                continue
               
            for nei, nc in graph[node]:
                queue.append((nei, stops + 1, costSoFar + nc))
               
        return minCost if minCost != float('inf') else -1