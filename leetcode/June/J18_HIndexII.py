class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        print(citations)
        for i in range(len(citations), 0, -1):
            if citations[i - 1] >= i:
                return i
        return 0

'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 0:
            return 0
        if n == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1
            
        i,j = 0, n - 1
        
        while(i<j):
            m = i + (j-i+1) // 2
            if citations[m] > n-m:
                j = m-1
            else:
                i = m
                
        if citations[j] > n-j:
            return n
        
        if citations[j] == n-j:
            return n-j
        else:
            return n-j-1
'''