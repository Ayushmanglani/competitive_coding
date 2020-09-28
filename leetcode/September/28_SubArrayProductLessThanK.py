class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding window
        # move left while window product >= k
        # add (right - left + 1) if window < k
        
        if not nums or k <= 0:
            return 0
        
        n = len(nums)
        
        window = 1
        left = 0
        
        ret = 0
        
        for right in range(n):
            window *= nums[right]
            
            while left < right and window >= k:
                window //= nums[left]
                left += 1
            
            if window < k:
                ret += (right - left + 1)
        
        return ret