class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lt = len(t)
        ls = len(s)
        i = 0
        j = 0
        while j<lt and i<ls:
            if t[j] == s[i]:
                i += 1
            j += 1
        if i == ls:
            return True
        return False