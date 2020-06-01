class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        i = 1
        x = []
        for j in range(len(trust)):
            if trust[j][0] not in x:
                x.append(trust[j][0])
        m = 0
        for i in range(1,N+1):
            if i not in x:
                m = i
                break
        if m!=0:
            c = 0
            for j in range(len(trust)):
                if trust[j][1] == m:
                    c += 1    
            if c == N-1:
                return(m)
            else:        
                return (-1)
        else:
            return (-1)
