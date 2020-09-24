class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freqT = [0]*26
        for i in t:
            freqT[ord(i)-97] += 1
            
        for i in s:
            freqT[ord(i)-97] -= 1
            
        for i in range(26):
            if freqT[i] == 1:
                return chr(i+97)

class Solution:
    from collections import Counter
    def findTheDifference(self, s: str, t: str) -> str:
        
        s = Counter(s)
        t = Counter(t)
        for k, v in t.items():
            if k not in s or s[k]!=v:
                return k                            