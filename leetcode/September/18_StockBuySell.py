class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minimum,maxglobal = prices[0],0
        
        for i in range(1,len(prices)):
            minimum = min(minimum,prices[i])
            if prices[i]>minimum:
                maxglobal = max(maxglobal, prices[i]-minimum)
        return maxglobal