class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return(" ".join(s[::-1]))

#method 2
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = s[::-1]
        res = ""
        for i in s:
            if i != "":
                res += i + " "
        return(res.strip())