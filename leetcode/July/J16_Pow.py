class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        else:
            res = 1.0
            if n < 0: 
                x = 1 / x 
                n = -n
            while n > 0:
                if n % 2 == 1:
                    res = res * x
                x *= x
                n//=2
            return res

#method 2
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n