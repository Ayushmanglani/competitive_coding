class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums:
            for i in range(len(nums)):
                if target<=nums[i]:
                    return i
            return(i+1)
        return 0