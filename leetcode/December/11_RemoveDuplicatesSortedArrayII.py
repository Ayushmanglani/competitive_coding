class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        k = nums[0]
        count = 1
        i = 1
        delete = 0
        while i+delete<n:
            if nums[i] == k:
                count += 1
            else:
                count = 1
                k = nums[i]
                
            if count>2:
                nums.pop(i)
                i -= 1
                count-=1
                delete += 1            
            i += 1
        print(nums)
        return len(nums)