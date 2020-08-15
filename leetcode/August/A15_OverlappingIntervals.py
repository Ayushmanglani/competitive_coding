class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: x[1])
        n, count = len(intervals), 1
        if n == 0: return 0
        curr = intervals[0]
        
        for i in range(n):
            if curr[1] <= intervals[i][0]:
                count += 1
                curr = intervals[i]
                
        return n - count  


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[0])
        start, end = intervals[0]
        print(start, end)
        res = 0
        for i in range(1, len(intervals)):
            intstart, intend = intervals[i]
            if intstart < end:
                res += 1
                end = min(end, intend)
            else:
                start = intstart
                end = intend
        return res
                