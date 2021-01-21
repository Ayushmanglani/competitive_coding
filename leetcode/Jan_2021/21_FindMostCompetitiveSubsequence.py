class Solution(object):
    def mostCompetitive(self, nums, k):
        attempts = len(nums) - k
        stack = []
        for num in nums:
            while stack and num < stack[-1] and attempts > 0:
                stack.pop()
                attempts -= 1
            stack.append(num)
        
        return stack[:k]