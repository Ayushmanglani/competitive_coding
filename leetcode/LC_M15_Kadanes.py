import numpy as np
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        A = np.multiply(A,-1)
        maxglobal1 = maxsum = A[0]
        for i in range(1,len(A)):
            maxsum = max(A[i], (maxsum+A[i]))
            if maxglobal1 < maxsum:
                maxglobal1 = maxsum
        arraysum = np.sum(A)
        A = np.multiply(A,-1)
        maxglobal = maxsum = A[0]
        for i in range(1,len(A)):
            maxsum = max(A[i], (maxsum+A[i]))
            if maxglobal < maxsum:
                maxglobal = maxsum
        res = maxglobal1-arraysum
        if maxglobal1-arraysum == 0 or arraysum == 0:
            return(max(max(A),maxglobal))
        return(max(np.sum(A),max(A),res,maxglobal))