class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(30, -1, -1):
            mySet = set()
            res <<= 1
            res += 1
            isValid = False
            for num in nums:
                if (num >> i) in mySet:
                    isValid = True
                    break
                mySet.add((num >> i) ^ res)
            if not isValid:
                res -= 1
        return res

class Solution:
    def findMaximumXOR(self, nums):
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            found = set([num & mask for num in nums])                
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:
                    ans = start
                    break         
        return ans        