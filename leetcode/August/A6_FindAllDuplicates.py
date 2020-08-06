class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        new = {}
        for i in nums:
            if i in new:
                res.append(i)
            else:
                new[i] = 1
        return(res)