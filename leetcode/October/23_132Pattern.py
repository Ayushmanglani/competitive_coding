class Solution(object):
    def find132pattern(self, nums):
        if(len(nums)<=2):return False
        mnv=[nums[0]] #minimum value
        for i in range(1,len(nums)):
            mnv.append(min(nums[i],mnv[-1]))
        stk=[] #stack
        j=len(nums)-1
        while(j>0):
            while(stk and stk[-1]<nums[j]):
                if(mnv[j-1]<stk[-1]):
                    return True
                stk.pop()
            stk.append(nums[j])
            j-=1
        return False