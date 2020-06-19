class Solution:
    def RabinKarp(self,text, M, q):
        if M == 0: return True
        h,t,d = 1,0,256

        dic = defaultdict(list)
        for i in range(M-1):  h = (h * d) % q 

        for i in range(M): 
            t = (d * t + ord(text[i]))% q

        dic[t].append(i-M+1)

        for i in range(len(text) - M):
            t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
            dic[t].append(i+1)

        for key in dic:
            for i,j in combinations(dic[key], 2):
                if text[i:i+M] == text[j:j+M]:
                    return (True, text[i:i+M])

        return (False, "")

    def longestDupSubstring(self, S: str) -> str:
        beg, end = 0, len(S)
        q = (1<<31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end)//2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found