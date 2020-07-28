class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        if len(s) == 1:
            return (ord(s[-1])-64)
        l = len(s)
        for i in range(l):
            res += (26**(l-i-1))*(ord(s[i])-64)
        return res

class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i,_str in enumerate(s[::-1]):
            res += (26**(i))*(ord(_str)-64)
        return res
