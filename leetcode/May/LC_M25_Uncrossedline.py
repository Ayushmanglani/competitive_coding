class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return
        la,lb = len(A),len(B)
        dp = [[0] * (lb+1) for _ in range(la+1)]
        # print(dp)
        for i in range(la):
            for j in range(lb):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])          
        return(dp[la][lb])
        