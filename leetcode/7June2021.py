class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        step = [0]*n
        
        step[0],step[1] = cost[0],cost[1]
        
        for i in range(2,n):
            step[i] = cost[i] + min(step[i-1], step[i-2])
            
        return(min(step[-1],step[-2]))
