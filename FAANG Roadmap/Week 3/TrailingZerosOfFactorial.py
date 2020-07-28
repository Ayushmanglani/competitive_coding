class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        x = 5
        while n >= x:
            res += n//x
            x *= 5
        return res


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n:
            n //= 5
            result += n
        return result        