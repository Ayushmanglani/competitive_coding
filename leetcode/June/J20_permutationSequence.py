class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ''
        a = []
        for i in range(1,n+1):
            a.append(i)
        fact = [0]*(n+1)
        fact[0] = 1
        for i in range(1,n+1):
            fact[i] = i*fact[i-1]
        # print(fact)
        k -= 1
        for i in range(n-1,-1,-1):
            p = k//fact[i]
            res += str(a[p])
            for j in range(p,n-1):
                a[j] = a[j+1]
            k = k% fact[i]
        return(res)