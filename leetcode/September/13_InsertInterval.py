class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res  = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        res.append(newInterval)
        return res

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        found = False
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals = intervals[:i] + [newInterval] + intervals[i:]
                found = True
                break
        
        if not found:
            intervals.append(newInterval)
        
        merged = []
        for interval in intervals:
            if len(merged) != 0 and merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        
        return merged        