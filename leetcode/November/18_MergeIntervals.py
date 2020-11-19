class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)
        for i in range(1,n):
            if res[-1][0] <= intervals[i][0] <= res[-1][1]:
                new = [min(res[-1][0],intervals[i][0]),max(res[-1][1],intervals[i][1])] 
                res.pop()
                res.append(new)
            else:
                res.append(intervals[i])
        return res