class Solution(object):
    def multiply(self, num1, num2):
        n1 = 0
        for n in num1:
            n1 = n1*10 + (ord(n)-48)
        n2 = 0
        for n in num2:
            n2 = n2*10 + (ord(n)-48)            
        print(n1,n2)
        return(str(n1*n2))