class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        diff = [prices[i+1] - prices[i] for i in range(n-1)]
        dp, dp_max = [0]*(n + 1), [0]*(n + 1)
        for i in range(n-1):
            dp[i] = diff[i] + max(dp_max[i-3], dp[i-1])
            dp_max[i] = max(dp_max[i-1], dp[i])
        print(dp,dp_max)
        return dp_max[-3]