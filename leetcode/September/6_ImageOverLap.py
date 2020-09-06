class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        # keep track of the i,j coordinates where we have a 1 in both matrices: O(n**2)
        A1s = []
        B1s = []
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    A1s.append((i, j))
                
                if B[i][j] == 1:
                    B1s.append((i, j))                    
        # for each i,j coordinate that is 1 in both A and B, find the delta between
        # the i and j coordinates (here by subtracting bi from ai and bj from aj)
        # and keep track of these: O(n**2)
        mem = {}
        for ai, aj in A1s:
            for bi, bj in B1s:
                k = (ai-bi, aj-bj)
                if k in mem:
                    mem[k] += 1
                else:
                    mem[k] = 1                
        # return our max coordinate if we have on else 0: O(n)
        return max(mem.values() or [0])