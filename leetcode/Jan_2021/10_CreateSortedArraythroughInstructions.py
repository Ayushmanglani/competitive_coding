from collections import defaultdict
class Solution(object):
    def createSortedArray(self, instructions):
        maxVal = max(instructions)
        count = defaultdict(int)  # binary indexed tree is 1-indexed/use a dict to save some space

        def add2tree(num):
            while num <= maxVal:
                count[num] += 1
                num += num & -num
                
        def getTotalSmaller(num):
            smaller = 0
            while num > 0:
                smaller += count[num]
                num -= num & -num
            return smaller
        
        rst = 0
        for total, num in enumerate(instructions):
            total = total + 1
            add2tree(num)
            rst += min(getTotalSmaller(num - 1), total - getTotalSmaller(num))
        return rst % (10**9 + 7)