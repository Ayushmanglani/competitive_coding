class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        dpn = [0]*n
        dpn[0] = nums[0]
        
        for i in range(1,n):
            if nums[i] > 0:
                dp[i] = max(nums[i],nums[i]*dp[i-1])
                dpn[i] = nums[i]*dpn[i-1]
            else:
                dp[i] = dpn[i-1]*nums[i]
                dpn[i] = min(nums[i]*dp[i-1],nums[i])
        return max(dp)