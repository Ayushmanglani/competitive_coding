class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x^y
        c = 0
        while xor>0:
            if xor%2 != 0:
                c += 1
            xor = xor//2
        return(c)

#method 2:
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def DecimalToBinary(num):    
            s = ""
            while num > 0:
                s += str(num%2)
                num = num//2
            return s[::-1]
        dx = DecimalToBinary(x)
        dy = DecimalToBinary(y)
        lx = len(dx)
        ly = len(dy)
        c = 0
        if lx>ly:
            l = lx-ly
            c += dx[:l].count('1')
            dx = dx[l:]
            l = ly
        elif lx<ly:
            l = ly-lx
            c += dy[:l].count('1')
            dy = dy[l:]
            l = lx
        for i in range(len(dx)):
            if dx[i] != dy[i]:
                c+=1
        return(c)