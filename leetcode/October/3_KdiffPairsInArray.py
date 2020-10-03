class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        lookup = Counter(nums)
        ans = 0
        for x in lookup: 
            if k > 0 and x + k in lookup: 
                ans+=1
            elif k == 0 and lookup[x] > 1: 
                ans += 1 
        return ans

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:        
        nums.sort()
        total = 0
        x = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                d = nums[j]-nums[i]
                if d == k and nums[i] not in x:
                    x.append(nums[i])
                    total += 1
                elif d>k:
                    break
        return total        