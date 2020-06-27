class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return n
        T = [0]*(n+1)
        T[0] = T[1] = 1
        for i in range(2,n+1):
            for j in range(0,i):
                T[i] += T[j]*T[i-j-1]
        return(T[n])