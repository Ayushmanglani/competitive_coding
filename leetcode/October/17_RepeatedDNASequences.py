class Solution(object):
    def findRepeatedDnaSequences(self, s):
        res = set()
        seen = set()
        for i in range(len(s)-9):
            cur = s[i:i+10]
            if cur in seen:
                res.add(cur)
            else:
                seen.add(cur)
        return list(res)