class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i,n in enumerate(nums):
            num_map[n] = i 
        for i in range(len(nums)):
            s = target-nums[i]
            if s in num_map and i != num_map[s]:
                return([i,num_map[s]])