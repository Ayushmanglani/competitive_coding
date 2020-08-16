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

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell1, sell2, buy1, buy2 = 0, 0, -999999, -999999
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2        