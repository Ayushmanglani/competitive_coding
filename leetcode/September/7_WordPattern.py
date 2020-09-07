class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        A = str.split(" ")
        dic = {}
        la = len(A)
        if la != len(pattern):
            return False
        for i in range(la):
            if pattern[i] in dic:
                if dic[pattern[i]] != A[i]:
                    return False
            else:
                if A[i] in dic.values():
                    return False
                dic[pattern[i]] = A[i]
        return True