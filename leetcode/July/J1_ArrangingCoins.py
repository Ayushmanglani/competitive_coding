class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 1: return n

        c = (8*n + 1) ** 0.5
        b = ((c-1)/2)
        
        return math.floor(b)      

    '''
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, 65536
        while l < r:
            mid = (l + r) >> 1
            if mid * (mid + 1) // 2 <= n:
                l = mid + 1
            else:
                r = mid
        return l - 1
    def arrangeCoins(self, n: int) -> int:
    	i = 1
        while n>0:
            n -= i
            i += 1
        if n == 0:
            return(i-1)
        return(i-2)