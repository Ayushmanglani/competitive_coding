class Solution(object):
    def concatenatedBinary(self, n):
        res = ''
        for i in range(1,n+1):
            res += bin(i)[2:]
        return(int(res,2) %(10**9+7))

class Solution(object):
    def concatenatedBinary(self, n):
        ans, M = 0, 10**9 + 7
        for x in range(n):
            ans = (ans * (1 << (len(bin(x+1)) - 2)) + x+1) % M
        return ans        