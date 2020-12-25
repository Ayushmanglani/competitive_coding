class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        result = []
        N = len(matrix)
        M = len(matrix[0])
        #Iterate over heads
        for d in range(M + N - 1):
            inter = []
            if d < M:
                row = 0
                col = d
            else:
                row = d - M + 1
                col = M - 1
                
            #Diagonal Traversal
            while row < N and col > -1:
                inter.append(matrix[row][col])
                row += 1
                col -= 1  
            if d % 2 == 0:
                inter.reverse()
                result += inter
            else:
                result += inter
        return result


class Solution(object):
    def findDiagonalOrder(self, matrix):
        res = []
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            j = 0
            new = []
            rev = False
            if i%2 == 0:
                rev = True
            while 0<=j<m and 0<=i<n:
                new.append(matrix[j][i])
                j += 1
                i -= 1
            if rev == True:
                res += new[::-1]
            else:
                res += new
        for i in range(1,m):
            j = n-1
            new = []
            rev = False
            if n%2 !=0 and i%2 == 0:
                rev = True
            if n%2 ==0 and i%2 != 0:
                rev = True
            while 0<=j<n and 0<=i<m:
                new.append(matrix[i][j])
                j -= 1
                i += 1
            if rev == True:
                res += new[::-1]
            else:
                res += new
        return res        