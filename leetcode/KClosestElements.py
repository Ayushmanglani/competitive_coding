#Find K Closest Elements
class Solution(object):
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        if n == k:
            return arr
        
        new = []
        for e in arr:            
            new.append([e,abs(e-x)])
            
        new = sorted(new, key=lambda x: x[1])
        
        res = []
        for i in range(k):
            res.append(new[i][0])
        
        res.sort()
        return res
