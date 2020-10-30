class Solution(object):
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        
        longest = [1] * len(nums)
        number = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if longest[j] + 1 > longest[i]:
                        longest[i] = longest[j] + 1
                        number[i] = number[j]
                    elif longest[j] + 1 == longest[i]:
                        number[i] += number[j]
        
        longestSub = max(longest)
        ans = 0
        for num in range(len(number)):
            if longest[num] == longestSub:
                ans+=number[num]
    
        return ans

        