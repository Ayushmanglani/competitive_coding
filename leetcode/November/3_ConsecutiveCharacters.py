class Solution(object):
    def maxPower(self, s):
        pwr = [0]*26
        c = s[0]
        k = 1
        for i in range(1,len(s)):
            if c == s[i]:
                k += 1
            else:
                pwr[ord(c)-97] = max(pwr[ord(c)-97],k)
                c = s[i]
                k = 1
        pwr[ord(c)-97] = max(pwr[ord(c)-97],k)                                
        #print(pwr)
        return max(pwr)