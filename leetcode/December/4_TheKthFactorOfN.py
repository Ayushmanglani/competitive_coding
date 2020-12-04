class Solution(object):
    def kthFactor(self, n, k):
        factors = []
        for i in range(1,n+1):
            if n%i == 0:
                factors.append(i)
        try:
            return factors[k-1]
        except:
            return -1

class Solution(object):
    def kthFactor(self, n, k):
        i = 1
        lt = []
        ls = []
        
        while(i**2 < n):
            if n % i == 0:
                lt.append(i)
                ls.append(n//i)
            i += 1
            
        if i**2 == n:
            lst = lt + [i] + ls[::-1]
        else:
            lst = lt + ls[::-1]
            
        if k <= len(lst):
            return (lst)[k-1]
        return -1            