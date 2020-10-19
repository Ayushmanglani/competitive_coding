class Solution(object):
    def minDominoRotations(self, A, B):
        n = len(A)
        
        countA = [0]*7
        for v in A:
            countA[v] += 1
        #print(countA)
        maxa = max(countA)
        va = countA.index(maxa)
        #print(va)
        
        countB = [0]*7
        for v in B:
            countB[v] += 1
        #print(countB)
        maxb = max(countB)
        vb = countB.index(maxb)
        #print(vb)
        
        ta = 0
        for i in range(n):
            if A[i] != va and B[i] == va:
                ta += 1
        
        tb = 0
        for i in range(n):
            if B[i] != vb and A[i] == vb:
                tb += 1
                
        if ta + maxa == n and tb + maxb == n:
            return(min(ta,tb))
        elif ta + maxa == n:
            return ta
        elif tb + maxb == n:
            return tb
        else:
            return -1