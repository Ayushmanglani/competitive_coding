def rec(s,k):
    if len(s) <= k:
        return
    minInd = s.index(min(s[:k+1]))
    x.append(s[minInd])
    s1 = s[minInd+1:]
    rec(s1,k-minInd)
    
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        global x
        x = []
        if len(num) == k:
            return(""""""+str(0)+"""""")
        rec(num,k)
        return(str(int("".join(x))))