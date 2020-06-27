import math
class Solution:
    def numSquares(self, n: int) -> int:
        a = [0]*(n+1)
        for i in range(1,n+1):
            r = math.sqrt(i)
            if r.is_integer():
                a[i] = 1
            else:
                r = int(r)
                ind = i - (r*r)
                v1 = 1+a[ind]
                v2 = v1
                for j in range(1,r):
                    d = (r-j)*(r-j)
                    try:
                        nv = i//d + a[(i%d)]
                    except:
                        nv = v1
                    if v2 > nv:
                        v2 = nv
                a[i] = min(v1,v2)
        # print(a)
        return(a[-1])