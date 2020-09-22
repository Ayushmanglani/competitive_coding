from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        T = n//3
        res = []
        for i in count:
            if count[i]>T:
                res.append(i)
        return res