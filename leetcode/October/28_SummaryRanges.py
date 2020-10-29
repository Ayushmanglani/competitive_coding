class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return
        res = [str(nums[0])]
        for i in range(1,len(nums)):
            ress = res[-1].split("->")
            if int(ress[-1])+1 == nums[i]:
                if "->" in res[-1]:
                    new = ress[0]+"->"+str(nums[i])
                else:
                    new = res[-1]+"->"+str(nums[i])
                res.pop()
                res.append(new)
            else:
                res.append(str(nums[i]))
        return res