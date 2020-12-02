class Solution(object):
    def isAnagram(self, s, t):
        freqs = [0]*26
        for l in s:
            freqs[ord(l)-97] += 1
        for l in t:
            freqs[ord(l)-97] -= 1
        if max(freqs) != 0 or min(freqs) != 0:
            return False
        return True
        '''
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False
        '''