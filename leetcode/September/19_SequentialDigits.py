class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ls = len(str(low))
        lh = len(str(high))
        res = []
        s='123456789'
        for l in range(ls,lh+1):
            for j in range(0,9-l+1):
                n = int(s[j:j+l])
                if low <= n <= high:
                    res.append(n)
        return res

class Solution:
    def sequentialDigits(self, low, high):
        answer=[]
        for i in range(1,10):
            number=i
            next=i
            while(number<=high and next<10):
                if number>=low:
                    answer.append(number)
                next=next+1
                number=number*10+next
        return sorted(answer)        