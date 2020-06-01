class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        count = sorted(count.items(), key=lambda i: i[1], reverse=True)
        s = ''
        for i in range(len(count)):
            s += count[i][0] * count[i][1]
        return(s)