class Solution(object):
    def smallestDivisor(self, nums, threshold):
        l, h = 1, max(nums)+1
        while l <= h:
			m = (l + h)//2
			res = sum(n//m + bool(n%m) for n in nums)
			if res > threshold:
				l = m+1
			elif res <= threshold:
				h = m-1
        return l

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        compute_sum = lambda x : sum([ceil(n / x) for n in nums])
        
        # search boundaries for the divisor
        left, right = 1, 2
        while compute_sum(right) > threshold:
            left = right
            right <<= 1
        
        # binary search
        while left <= right:
            pivot = (right + left) >> 1
            num = compute_sum(pivot)

            if num > threshold:
                left = pivot + 1
            else:
                right = pivot - 1
        
        # at the end of loop, left > right,
        # compute_sum(right) > threshold
        # compute_sum(left) <= threshold
        # --> return left
        return left


                