class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        dp = [0]*l
        if l == 0:
            return 0
        if l < 3:
            return max(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0]+nums[2]
        for i in range(3,l):
            dp[i] = nums[i]+max(dp[i-2],dp[i-3])
        # print(dp)
        return max(dp[-1],dp[-2])