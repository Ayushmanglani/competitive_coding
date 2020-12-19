class Solution:
    def cherryPickup(self, grid):
        M, N = len(grid[0]), len(grid)

        dp = [[[-10**9] * (M+2) for _ in range(M+2)] for _ in range(N)]
        dp[0][1][M] = grid[0][0] + grid[0][M-1]
        for j in range(1, N):
            for i1, i2 in product(range(1, M+1), range(1, M+1)):
                cand_prev = []
                for shift1, shift2 in product([-1,0,1], [-1,0,1]):
                    cand_prev.append(dp[j-1][i1 + shift1][i2 + shift2])
                    dp[j][i1][i2] = (grid[j][i1-1] + grid[j][i2-1])//(1 + (i1 == i2)) + max(cand_prev)

        return max(list(map(max, *dp[-1]))) 