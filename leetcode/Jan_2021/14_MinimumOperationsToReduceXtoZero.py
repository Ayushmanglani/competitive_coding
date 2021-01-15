class Solution(object):
    def minOperations(self, nums, x):
        sums = sum(nums)
        if x>sums:
            return -1
        if x==sums:
            return len(nums)
        
        sums = sums-x
        cur, start, ans = 0, 0, -1
        
        for end in range(len(nums)):
            if cur < sums:
                cur+=nums[end]
            
            while cur>=sums:
                if cur==sums:
                    ans = max(ans, end-start+1)
                cur -= nums[start]
                start+=1
        
        return len(nums)-ans if ans!=-1 else an

class Solution(object):
    def minOperations(self, nums, x):
        arr_sum = sum(nums)
        if arr_sum < x:
            return -1
        if arr_sum == x:
            return len(nums)
        
        required_subarray_sum = arr_sum - x
        left = curr_sum = max_subarray_size = 0
        for right, num in enumerate(nums):
            curr_sum += num
            while curr_sum > required_subarray_sum:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == required_subarray_sum:
                max_subarray_size = max(max_subarray_size, right - left + 1)
                
        return len(nums) - max_subarray_size if max_subarray_size > 0 else -1        