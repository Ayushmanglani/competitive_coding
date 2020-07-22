class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=numRows or numRows == 1:
            return s    
        a = [[] for _ in range(numRows)]
        m = numRows - 2
        k = 0
        f = 1
        for i in range(len(s)):
            if k==numRows and m!=0:
                if f==m:
                    a[numRows-1-m].append(s[i])
                    f = 1
                    k = 0
                    continue
                if f<m:    
                    a[numRows-1-f].append(s[i])
                    f += 1
            else:
                a[k%numRows].append(s[i])
                k += 1
        print(a)
        res = ""
        for i in range(numRows):
            for j in range(len(a[i])):
                res += a[i][j]
        return(res)