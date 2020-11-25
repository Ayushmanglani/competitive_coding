class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if K % 2 == 0 or K % 5 == 0: return -1
        r = 0
        for N in xrange(1, K + 1):
            r = (r * 10 + 1) % K
            if not r: return N

            