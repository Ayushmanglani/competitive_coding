class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        soln = {}
        for i in range(0,len(nums)):
            if(target-nums[i] in soln):
                return[soln[target-nums[i]],i]
            else:
                soln[nums[i]]=i
        return ans