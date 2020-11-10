class Solution(object):
    def flipAndInvertImage(self, A):
        m = len(A)
        n = len(A[0])
        h = n//2
        for i in range(m):
            for j in range(h):
                A[i][j],A[i][n-1-j] = A[i][n-1-j],A[i][j]
            for j in range(n):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return(A)