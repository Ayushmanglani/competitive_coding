class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums==[]:
            return 1
        s = set(nums)
        for i in range(1,len(nums)+2): #[1]
            if i not in s:
                return i
                break