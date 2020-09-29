class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        n = len(s)
        DP = [False] * (n+1)
        DP[0] = True
        for i in range(1, n+1):
            for word in wordDict:
                if DP[i-1] and i-1+len(word) <= n and s[i-1 : i-1+len(word)] == word:
                    DP[i-1+len(word)] = True
        return DP[n]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        new_dict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

                class Solution():
    def wordBreak(self, s, wordDict):
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            # return True when there is some combination that can generate s[i:]
            if i == len(s):
                return True
            else:
                res = False
                for word in wordDict:
                    if len(word) <= len(s) - i:
                        if word == s[i: i + len(word)]:
                            res = res or dfs(i + len(word))
                memo[i] = res
                return res
        return dfs(0)