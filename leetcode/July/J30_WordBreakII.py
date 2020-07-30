class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        if not n:
            return []
        letters = set(c for c in s)
        letterw = set(c for word in wordDict for c in word)
        if not letterw.issuperset(letters):
            return []
        
        # if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
        #     return []
        
        dp = [[] for _ in range(n)]
        for i in range(0, n):
            for j in range(0, i+1):
                cur_word = s[j:i+1]
                if cur_word in wordDict:
                    if j == 0:
                        dp[i].append(cur_word)
                    else:
                        for sentence in dp[j-1]:
                            dp[i].append(sentence +" "+ cur_word)
        print(dp)
        return(dp[n-1])