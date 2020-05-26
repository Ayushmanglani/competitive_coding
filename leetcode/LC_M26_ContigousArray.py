class Solution(object):
    def findMaxLength(self, nums):
        M = count =0
        dic = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count == 0:
                M = i+1
            if count in dic:
                M = max(M, i-dic[count])
            else:
                dic[count] = i
        return(M)