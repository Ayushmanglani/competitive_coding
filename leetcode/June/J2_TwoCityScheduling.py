class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s = 0
        l = len(costs)//2
        costs = sorted(costs, key=lambda i: abs(i[1]-i[0]))
        n1 = n2 = 0
        for i in range(len(costs)-1,-1,-1):
            if costs[i][0] < costs[i][1]:
                if n1<l:
                    s += costs[i][0]
                    n1 += 1
                else:
                    s += costs[i][1]
                    n2 += 1
            elif costs[i][0] > costs[i][1]:
                if n2<l:
                    s += costs[i][1]
                    n2 += 1
                else:
                    s += costs[i][0]
                    n1 += 1
            else:
                s += costs[i][0]
        return s