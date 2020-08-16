class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits, lowest, highest, maxProfit = [], float('inf'), -float('inf'), 0
        for p in prices:
            if p < lowest:
                lowest = p
            maxProfit = max(maxProfit, p-lowest)
            profits.append(maxProfit)
        maxProfit = 0
        for i in range(len(profits)-1, -1, -1):
            if prices[i] > highest:
                highest = prices[i]
            maxProfit = max(maxProfit, (highest - prices[i]) + (profits[i-1] if i > 0 else 0))
        return maxProfit