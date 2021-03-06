class Solution(object):
    def missingNumber(self, nums):
        m = max(nums)
        a = [-1]*(m+1)
        for n in nums:
            a[n] = 0
        for i in range(m+1):
            if a[i] == -1:
                return i
        return m+1

class Solution(object):
    def missingNumber(self, nums):
        length = len(nums)
        total = sum(nums)
        max_ = sum(range(1, length+1))
        
        return max_ - total