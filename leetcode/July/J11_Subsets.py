class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums,0,[],ans)
        return ans
    def helper(self,nums,index,path,ans):
        ans.append(path)
        for i in range(index,len(nums)):
            self.helper(nums,i+1, path + [nums[i]],ans)

#Method 2
from itertools import combinations 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        x = [[]]
        l = len(nums)          
        for j in range(1,l+1):
            comb = combinations(nums, j) 
            for i in list(comb): 
                if list(i) not in x:
                    x.append(list(i))
        return(x)
