class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)    
        ans = 0
        for i,c in enumerate(citations, 1):
            print(c,i)
            if c >= i: ans = i
        return ans 