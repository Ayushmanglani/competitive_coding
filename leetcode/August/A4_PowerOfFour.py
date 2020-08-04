#16ms
class Solution:
    def isPowerOfFour(self, num):
        if num<= 0:
            return False
        z = bin(num)[::-1]
        if z.count('1') > 1:
            return False
        p = z.index('1')
        return p % 2 == 0

#52ms
import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num > 0:
            l = math.log2(num)/2
            if l - int(l) == 0.0:
                return True
        return False        