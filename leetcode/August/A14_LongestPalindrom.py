from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        take = 0
        for i in count:
            if count[i]%2 == 0:
                res += count[i]
            elif count[i]%2 != 0 and count[i]>2:
                res += (count[i]-1)
                if take == 0:
                    res += 1
                    take = 1
            elif count[i] == 1 and take == 0:
                res += 1
                take = 1
        return res

from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        for i in count.values():
            ans += i //2 * 2
            if ans % 2 == 0 and i % 2 == 1:
                ans += 1
        return ans