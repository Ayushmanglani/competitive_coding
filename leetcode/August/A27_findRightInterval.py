class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        n = len(intervals)
        if not intervals: return[]
        biggist = - math.inf
        res = [-1] * n
        for i, item in enumerate(intervals):
            x = item[0]
            y = item[1]
            if x > biggist:
                biggist = x
            dic[x].append((y,i))
        for i, item in enumerate(intervals):
            begin = item[1]
            for p in range(begin,biggist + 1):
                for j in dic[p]:
                    x,y = j
                    res[i] = y
                    break
                if res[i] != -1:
                    break
        return res