class Solution(object):
    def mirrorReflection(self, p, q):
        k = 1
        while k*q%p: k += 1
        if k%2==1 and (k*q//p)%2==0: return 0
        if k%2==1 and (k*q//p)%2==1: return 1
        if k%2==0 and (k*q//p)%2==1: return 2 

class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        while p % 2 == 0 and q % 2 == 0:
            p /= 2
            q /= 2
        if p % 2 == 0:
            return 2
        if q % 2 == 0:
            return 0
        return 1        