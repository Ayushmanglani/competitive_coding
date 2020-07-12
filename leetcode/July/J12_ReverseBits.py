class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n).replace("0b","")
        s = (32 - len(s))*"0" +s
        return(int(s[::-1],2))


#Normal
class Solution:
    def reverseBits(self, n: int) -> int:
        s = ""
        while n>0:
            s += str(n%2)
            n = n//2
        k = 32 - len(s)
        e = "0"*k
        s = s+e
        return(int(s,2))