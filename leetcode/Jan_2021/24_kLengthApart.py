class Solution(object):
    def kLengthApart(self, nums, k):
        count = 0
        for i, n in enumerate(nums):        
            if n == 1 and i > 0:
                if count < k:
                    return False
                else:
                    count = 0
            else:
                count += 1        
        return True