class Solution(object):
    def getMaximumGenerated(self, n):
        if n<1:
            return 0
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            if i%2 == 0:
                dp[i] = dp[i//2]
            else:
                k = (i-1)//2
                dp[i] = dp[k]+dp[k+1]
        return max(dp)