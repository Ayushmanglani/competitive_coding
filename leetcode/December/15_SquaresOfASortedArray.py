class Solution(object):
    def sortedSquares(self, nums):
        mylist = []
        for i in nums:
            mylist.append(i**2)
        return sorted(mylist)


import bisect 
class Solution(object):
    def sortedSquares(self, nums):
        new = []
        n = len(nums)
        for i in range(n):
            if nums[i]<0:
                new.append(nums[i]*nums[i])
            else:
                break
        new = new[::-1]
        if len(new) == n:
            return new
        if new:
            M = new[-1]
        else:
            M = -9999
        for j in range(i,n):
            p = nums[j]*nums[j]
            if p >= M:
                new.append(p)
                M = p
            else:
                bisect.insort(new, p) 
        return new        