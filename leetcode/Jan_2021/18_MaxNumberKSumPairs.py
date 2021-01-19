class Solution(object):
    def maxOperations(self, nums, k):
        cnt, ans = Counter(nums), 0
        for val in cnt:
            ans += min(cnt[val], cnt[k - val])
        return ans//2
