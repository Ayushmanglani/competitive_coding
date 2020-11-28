class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        if len(nums) <= k:
            return [max(nums)]
        
        queue = deque()
        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        output = [queue[0]]
        print(queue)
        
        for end in xrange(k, len(nums)):
            start = end - k
            if nums[start] == queue[0]:
                queue.popleft()
            while queue and queue[-1] < nums[end]:
                queue.pop()
            queue.append(nums[end])
            output.append(queue[0])
        return output
        
        
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        a = nums[:k]
        print(a)
        max_here = max(a)
        maxarray = [max_here]
        n = len(nums)
        for i in range(k,n):
            if a.pop(0) == max_here:
                if a:
                    max_here = max(a)
                else:
                    max_here = -9999
            max_here = max(max_here,nums[i])
            a.append(nums[i])
            maxarray.append(max_here)
        return maxarray        