#Method 1
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))>1:
            res = 0
            while num>0:
                res += num%10
                num = num//10
            res += num
            num = res
        return num

#Method 2
class Solution:
    def addDigits(self, num: int) -> int:
        if num==0:
            return 0
        else: 
            return (num-1) %9 +1

#Method 3
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        
        while num >= 10:
            num = num // 10 + num % 10
            
        return num