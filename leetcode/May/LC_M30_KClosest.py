class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            res.append(((x*x) + (y*y),points[i]))
        res = sorted(res, key= lambda i: i[0])
        fin = []
        for i in range(K):
            fin.append(res[i][1])
        return fin