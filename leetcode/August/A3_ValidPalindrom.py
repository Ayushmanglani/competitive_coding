#Method 1 --> 48ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

#Method 2 --> 60ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ''
        i = 0
        while i<len(s):
            if 97<=ord(s[i])<=122:
                res += s[i]
            elif s[i].isdigit():
                res += s[i]
            i += 1
        if res == res[::-1]:
            return True