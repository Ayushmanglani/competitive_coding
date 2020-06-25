class Solution:
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = len(nums)
        if l>1:
            a = [0]*(l+1)
            for i in range(l):
                a[nums[i]] += 1
                if a[nums[i]] > 1:
                    return nums[i]