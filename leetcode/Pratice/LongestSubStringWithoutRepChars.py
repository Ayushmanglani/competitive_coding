class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        k = []
        for i in range(len(s)):
            if s[i] in k:
                if maxlength<len(k):
                    maxlength = len(k)
                j = k.index(s[i])
                k = k[j+1:]
            k.append(s[i])
        if maxlength == 0:
            return len(s)
        if len(k)>maxlength:
            return len(k)
        return maxlength