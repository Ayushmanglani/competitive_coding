class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        res = 1
        N = abs(n)
        while(N!=1):
            if N%2!=0:
                res = res*x
                N = N-1
            x = x*x
            N=N/2
        res = res*x
        if n < 0:
            return(1/res)
        return res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n        