from itertools import permutations 
        
class Solution(object):
    def countArrangement(self, N):
        self.res = 0
        def dfs(n,tmp,remain):
            if n==N+1:
                self.res+=1
            else:
                for i in range(len(remain)):                 
                    if remain[i]%n==0 or n%remain[i]==0:
                        dfs(n+1,tmp+[i],remain[:i]+remain[i+1:])
        dfs(1,[],[i+1 for i in range(N)])
        return self.res

        