class Solution(object):
    def countVowelStrings(self, n):
        dp = [[1] + [0 for _ in range(n)] for _ in range(5+1)]
        for i in range(4, -1, -1):
            for j in range(1, n+1):
                dp[i][j] = dp[i+1][j] + dp[i][j-1]
        print(dp)
        return dp[0][n]

class Solution(object):
    def countVowelStrings(self, n):
        dp = [[0 for _ in range(5)] for _ in range(n)]
        
        for i in range(5):
            dp[0][i] = i+1
            
        for i in range(1,n):
            for j in range(5):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]

class Solution(object):
    def countVowelStrings(self, n):        
        #x1 + x2 + x3 + x4 + x5 = n
        #y1 + y2 + y3 + y4 + y5 = n + 5 = m
        #k = 5
        
        #C(m - 1, k-1)
        k = 5
        m = n + k
        partial = long(1)
        for i in range(m - k + 1, m):
            partial *= long(i)
            
        partial /= 24
        
        return(partial)        
