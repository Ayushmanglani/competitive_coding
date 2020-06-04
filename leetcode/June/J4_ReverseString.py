class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        for i in range(l//2):
            s[i], s[-i-1] = s[-i-1], s[i]
        
        #s = s.reverse()