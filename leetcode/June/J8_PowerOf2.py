import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>=1 and math.log2(n).is_integer():
            return True
        return False

#Other Methods
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        i = 2
        while i <= n:
            if i == n:
                return True
            i *= 2
        return False

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n and not (n & (n - 1)))

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n == 1):
            return True
        if(n == 0):
            return False
        while n % 2 == 0:
            n = n//2
        if(n == 1):
            return True
        else:
            return False
'''