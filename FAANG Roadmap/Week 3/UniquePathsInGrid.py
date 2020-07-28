class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            grid[0][i] = 1
        for i in range(n):
            grid[i][0] = 1
        for r in range(1, n):
            for c in range(1, m):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        return grid[n-1][m-1]