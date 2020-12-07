class Solution(object):
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in xrange(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A

class Solution(object):
    def generateMatrix(self, n):
        try:
            result =  [[0] * n for i in range(n)]
            if n:
                for rep in range((n + 1) // 2):
                    for lr in range(rep, n - rep):
                        result[rep][lr] = result[rep][lr-1] + 1
                    for ub in range(rep+1, n-rep):
                        result[ub][-1 - rep]= result[ub-1][-1 - rep] + 1
                    for rl in range(rep+2, n-rep+1):
                        result[-1 - rep][-rl] = result[-1 - rep][1 - rl] + 1
                    for bu in range(rep+2, n-rep):
                        result[-bu][rep] = result[1 - bu][rep] + 1
            return result
        except:
            return []        