class Solution(object):
    def search(self, nums, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l + r)//2
            
            if nums[m] == t:
                return True
            
            # duplicate edge case [1,3,1,1,1]
            if nums[l] == nums[m]:
                l += 1
            elif nums[l] <= nums[m]:
                # check both the range check tis case (5,6,7, 0,1,2)
                if nums[l] <= t < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # check both the range instead of regular binary search
                if nums[m] < t <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return False

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target in nums:
            return True
        return False        