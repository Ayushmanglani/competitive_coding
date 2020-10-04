class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda i: i[0])
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][0] <= intervals[i][0] and intervals[i][1] <= res[-1][1]:
                continue
            if intervals[i][0] <= res[-1][0] and res[-1][1] <= intervals[i][1]:
                res.pop()
                res.append(intervals[i])
            else:
                res.append(intervals[i])
        return len(res)