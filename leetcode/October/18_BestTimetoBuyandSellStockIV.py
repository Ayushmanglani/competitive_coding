class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n<=1:return 0
        if k>=n/2:
            ans = 0
            for i in range(1,n):
                if prices[i]>prices[i-1]:
                    ans += prices[i]-prices[i-1]
            return ans
        
        pre = [0]*n
        K = k
        for k in range(1,K+1):
            cur = [0]*n
            mini = prices[0]
            for j in range(1,n):
                mini = min(mini,prices[j]-pre[j-1])
                cur[j] = max(cur[j-1],prices[j]-mini)
            pre = cur
        return pre[n-1]