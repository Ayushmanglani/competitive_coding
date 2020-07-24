class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        minimum,profit = prices[0],0
        
        for i in range(1,len(prices)):
            minimum = min(minimum,prices[i])
            if prices[i]>minimum:
                profit = max(profit, prices[i]-minimum)
        return profit