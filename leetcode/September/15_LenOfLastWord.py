class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        res = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                return res
            else:
                res += 1
        return res

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        return len(s[-1])        