class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        times = minutesToTest//minutesToDie + 1
        return int(ceil(log(buckets, times)))        