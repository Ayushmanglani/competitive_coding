class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1: return list(range(10))
        ans = []
        
        def process(i, n):
            if n == N:
                ans.append(i)
            else:
                x = i % 10
                if x + K < 10:
                    process(i * 10 + x + K, n+1)
                if K != 0 and x - K >= 0:
                    process(i * 10 + x - K, n+1)       
        
        for i in range(1, 10):
            if i + K < 10 or i - K >= 0:
                process(i, 1)
        
        return ans