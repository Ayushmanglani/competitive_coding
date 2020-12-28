class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        k = 0
        sum = 0
        while sum < target:
            k += 1
            sum += k
        d = sum - target
        if d % 2 == 0:
            return k
        return k + 1 + (k % 2)

class Solution(object):
    def reachNumber(self, target):
        t = abs(target)
        n = math.floor(math.sqrt(2*t))
        while True:
            to_minus = ((n+1)*n)/2 - t 
            if to_minus >= 0:  
                if to_minus%2==0:
                    return int(n)
            n+=1        