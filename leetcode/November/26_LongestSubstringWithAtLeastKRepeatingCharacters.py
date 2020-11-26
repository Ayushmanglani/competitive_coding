class Solution(object):
    def longestSubstring(self, s, k):
        if len(s)<k:
            return 0
        c = min(set(s), key = s.count)
        
        if s.count(c)>=k:
            return len(s)
        else:
            return max( self.longestSubstring(sub,k) for sub in s.split(c))

class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) == 0 or k > len(s):
            return 0
        c = Counter(s)
        sub1, sub2 = "", ""
        for i, letter in enumerate(s):
            if c[letter] < k:
                sub1 = self.longestSubstring(s[:i], k)
                sub2 = self.longestSubstring(s[i+1:], k)
                break
        else:
            return len(s)
        return max(sub1, sub2)            