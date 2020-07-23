class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        res = []
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in dic:
            if dic[i] == 1:
                res.append(i)
        return res