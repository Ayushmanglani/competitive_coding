class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.ranges = [0]
        sm = 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)
        

    def pick(self) -> List[int]:
        n = random.randint(0, self.ranges[-1] - 1)
        i = bisect.bisect(self.ranges, n)
        x1, y1, x2, y2 = self.rects[i - 1]
        n -= self.ranges[i - 1]
        return [x1 + n % (x2 - x1 + 1), y1 + n // (x2 - x1 + 1)]


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.a = []
        self.l = rects
        cur = 0
        for x in rects:
            cur += (x[2] - x[0] + 1) *(x[3] - x[1] + 1)
            self.a.append(cur)
        print(self.a)

    def pick(self) -> List[int]:
        r = random.randint(1, self.a[-1])
        for i,x in  enumerate(self.a):
            if r <= x:
                k = self.l[i]
                return [random.randint(k[0], k[2]), random.randint(k[1], k[3])]        