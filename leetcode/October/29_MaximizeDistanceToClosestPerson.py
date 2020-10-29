class Solution(object):
    def maxDistToClosest(self, seats):
        n = len(seats)
        sit = [0]*n
        d = -1
        for i in range(n):
            if seats[i] == 1:
                sit[i] = 0
                d = 0
            elif d != -1:
                d += 1
                sit[i] = d
        d = -1
        for i in range(n-1,-1,-1):
            if seats[i] == 1:
                sit[i] = 0
                d = 0
            elif d != -1:
                d += 1
                if sit[i] == 0:
                    sit[i] = d
                else:                        
                    sit[i] = min(d,sit[i])
        return max(sit)

class Solution:
    def maxDistToClosest(self, array: List[int]) -> int:
        pos=[]
        n=len(array)
        for i in range(n):
            if array[i]==1:                    
                pos.append(i)
        ans=0
        if pos[0]!=0:                         
            ans=pos[0]
        for i in range(len(pos)-1):
            distance=pos[i+1]-pos[i]
            if distance>1:
                ans=max(ans,distance//2)
        if pos[-1]!=n-1:
            ans=max(ans,(n-pos[-1])-1)
        return (ans)                