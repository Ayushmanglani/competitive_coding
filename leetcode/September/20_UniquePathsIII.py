class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(x,y,total_blocks_travelled):
            if grid[x][y] == -1:
                return 0
            if grid[x][y] == 2:
                return 1 if total_blocks_travelled == total_viable_blocks - 1 else 0
            else:
                grid[x][y] = -1
                totalPaths = 0
                for add_x, add_y in [(0,1),(1,0),(0,-1),(-1,0)]:
                    if 0 <= x + add_x < n and 0 <= y + add_y < m and grid[x + add_x][y + add_y] != -1:
                        totalPaths += dfs(x + add_x, y + add_y, total_blocks_travelled + 1)
                grid[x][y] = 0
                return totalPaths
        n,m = len(grid), len(grid[0])
        total_viable_blocks = n*m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    total_viable_blocks -= 1
                if grid[i][j] == 1:
                    start = [i,j]
        return dfs(start[0], start[1], 0)    

class Solution: 
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m,n=len(grid),len(grid[0])
        
        # 1. profiling
        obs=0
        for r,row in enumerate(grid):
            for c,v in enumerate(row):
                if v==1: rs,cs=r,c # start
                elif v==-1: obs+=1 # obstacles
                elif v==2: re,ce=r,c # end 
                
        # 2. backtrack
        tot=m*n-obs-1 # total steps
        ans=0
        def backtrack(r=rs,c=cs,steps=0):
            nonlocal tot,m,n, ans
            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                rn,cn=r+dr,c+dc
                if not(0<=rn<m and 0<=cn<n and grid[rn][cn] in (0,2)):
                    continue
                if grid[rn][cn]==2:
                    if steps+1==tot:
                        ans+=1
                    continue                                            
                grid[rn][cn]=-1
                backtrack(rn,cn,steps+1)
                grid[rn][cn]=0
        backtrack()
        return ans
        