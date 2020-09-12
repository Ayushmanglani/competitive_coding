class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(nums,k,n,index,path,ans):
            if k < 0 or n < 0:
                return
            elif k == 0 and n == 0:
                ans.append(path)
                return
            else:
                for i in range(index,len(nums)):
                    dfs(nums,k-1,n-nums[i],i+1,path+[nums[i]],ans)        
        ans = []
        nums = range(1,10)
        dfs(nums,k,n,0,[],ans)
        return ans

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        l=list(combinations([i for i in range(1, 10)], k))
        for i in l:
            if sum(i)==n:
                res.append(list(i))
        return res        
