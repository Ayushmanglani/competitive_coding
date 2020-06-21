class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if List:
            m = len(dungeon)
            n = len(dungeon[0])
            dp = [[0] * n] * m
            for i in range(m)[::-1]:
                for j in range(n)[::-1]:
                    if i == m-1 and j == n-1:
                        dp[i][j] = max(1, 1-dungeon[i][j])
                    elif i == m-1:
                        dp[i][j] = max(1, dp[i][j+1]-dungeon[i][j])
                    elif j == n-1:
                        dp[i][j] = max(1, dp[i+1][j]-dungeon[i][j])
                    else:
                        dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
            return dp[0][0]