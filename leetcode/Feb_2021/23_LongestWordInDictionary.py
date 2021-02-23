class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def is_subseq(main: str, sub: str) -> bool:
            i, j, m, n = 0, 0, len(main), len(sub)
            while i < m and j < n and n - j >= m - i:
                if main[i] == sub[j]:
                    i += 1
                j += 1
            return i == m
        
        res = ''
        helper = sorted(d, key = lambda x: len(x), reverse = True)
        for word in helper:
            if len(word) < len(res): return res
            if ( not res or word < res )  and is_subseq(word, s):
                res = word
        return res