#Naive Approach O(n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        b = -1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                b = nums[i+1]
                break
        if b == -1:
            return nums[0]
        return b

#Using Binary Search O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = (lo+hi)//2
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[hi] >= nums[mid]:
                hi = mid
            else:
                lo = mid+1
        return nums[lo]