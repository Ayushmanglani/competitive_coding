class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if nums:
            a = {}
            for i in range(len(nums)):
                try:
                    a[nums[i]] += 1
                except:
                    a[nums[i]] = 1
                if a[nums[i]] == 3:
                    a.pop(nums[i])
            x = list(a)
            return(x[0])
        
#         return (sum(list(set(nums)))*3-sum(nums))//2