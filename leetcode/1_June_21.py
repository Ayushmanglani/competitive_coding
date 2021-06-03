class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        maxarea = 0
        
        def searchland(p,q,r):
            if p<0 or q<0 or p==m or q==n or grid[p][q] != 1:
                return r
            r += 1
            # print(r)
            grid[p][q] = -1
            r = searchland(p+1,q,r)
            r = searchland(p-1,q,r)
            r = searchland(p,q+1,r)
            r = searchland(p,q-1,r)
            return r
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = searchland(i,j,0)
                    print(res)
                    maxarea = max(maxarea, res)
        
        return maxarea
