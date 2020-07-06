#method 1
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        num = ""
        for i in range(len(digits)):
            num += str(digits[i])
        num = int(num)+1
        res = list(str(num))
        return(res)

#method 2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = len(digits) - 1
        while i >= 0 and digits[i] == 10:
            digits[i] = 0
            if i == 0:
                digits = [1] + digits
            else:
                digits[i-1] += 1
            i -= 1
        return digits

#method 3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = digits[0]
        for i in range(1,len(digits)):
            num = num*10
            num += digits[i]
        num += 1
        res = []
        while num>0:
            res.append(num%10)
            num = num//10
        return(res[::-1])