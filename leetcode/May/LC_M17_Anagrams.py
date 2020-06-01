import numpy as np
MAX = 26
def compare(arr1, arr2):
    z = np.subtract(arr1,arr2)
    # z = list(z)
    if z.count(0) != 26:
        return False
    return True
        
class Solution(object):
    def findAnagrams(self, s, p):
        M = len(p) 
        N = len(s) 
        if N<M:
            return
        countP = [0]*MAX
        countTW = [0]*MAX
        res = []
        for i in range(M): 
            (countP[ord(p[i])-97 ]) += 1
            (countTW[ord(s[i])-97 ]) += 1

        for i in range(M,N): 
            if compare(countP, countTW): 
                res.append(i-M)  
            (countTW[ ord(s[i])-97 ]) += 1 
            (countTW[ ord(s[i-M])-97 ]) -= 1 
            
        if compare(countP, countTW): 
            res.append(N-M)
        return res