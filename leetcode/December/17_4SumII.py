class Solution(object):
    def fourSumCount(self, A, B, C, D):
        total_sum = 0
        cache = {}
        for i in C:
            for j in D:
                key = i + j
                if key in cache:
                    cache[key] += 1
                else:
                    cache[key] = 1
        for i in A:
            for j in B:
                key = 0 - i - j
                if key in cache:
                    total_sum += cache[key]
        return total_sum

