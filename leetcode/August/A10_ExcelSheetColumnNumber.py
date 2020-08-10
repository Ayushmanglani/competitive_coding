class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        l = len(s)
        for i in range(l):
            res += (26**(l-i-1))*(ord(s[i])-64)
        return res