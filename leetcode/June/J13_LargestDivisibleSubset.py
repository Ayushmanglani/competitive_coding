class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        nums.sort()
        l = len(nums)
        divCount = [1 for i in range(l)]
        prev = [-1 for i in range(l)]
        
        maxValueIndex = 0
        for i in range(1,l):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    if divCount[i] < divCount[j]+1:
                        divCount[i] = divCount[j]+1 
                        prev[i] = j            
            if divCount[maxValueIndex] < divCount[i]:
                maxValueIndex = i
        res = []
        k = maxValueIndex
        while maxValueIndex >= 0:
            res.append(nums[maxValueIndex])
            maxValueIndex = prev[maxValueIndex]
        
        res.sort()
        return res