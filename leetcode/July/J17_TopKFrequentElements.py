from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = sorted(Counter(nums).items(), key = lambda i:i[1], reverse=True)
        res = []
        for i in range(k):
            res.append(count[i][0])
        return res