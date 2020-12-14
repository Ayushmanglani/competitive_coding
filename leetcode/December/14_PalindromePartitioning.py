#Method1
class Solution(object):
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1] 

#Method2
class Solution(object):
    def partition(self, s):
        self.re=[]
        def ispalindrome(e):
            return e==e[::-1]     

        def dfs(e,path):
            if not e:
                temp=[]
                for i in range(len(path)-1):
                    temp.append(s[path[i]:path[i+1]])
                self.re.append(temp)
                return
            for i in range(1,len(e)+1):
                if ispalindrome(e[:i]):
                    dfs(e[i:],path+[path[-1]+i])
        dfs(s,[0])
        return self.re

#Method3
class Solution(object):
    def partition(self, s):
        def isPalindrome(s):
            return s == s[::-1]
        
        dp = [[] for _ in range(len(s) + 1)]
        for end in range(1, len(s) + 1):
            tmp = []
            for start in range(end):
                if isPalindrome(s[start:end]):
                    if start == 0:
                        tmp.append([s[:end]])
                    elif dp[start]:
                        for each in dp[start]:
                            tmp.append(each + [s[start:end]])
            dp[end] = tmp
        return dp[-1]        