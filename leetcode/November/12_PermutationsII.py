class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        res = [[nums[0]]]
        
        for i in range(1, len(nums)):
            new_res = []
            for r in res:
                for j in range(len(r)+1):
                    new_res.append(r[0:j] + [nums[i]] + r[j:])
                    if j < len(r) and r[j] == nums[i]:
                        break
            res = new_res
        return res

from itertools import permutations 
class Solution(object):
    def permuteUnique(self, nums):
        permList = permutations(nums)
        return set(permList)        