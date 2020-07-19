class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_row, zero_col = set(), set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
                    
        for i in range(m):
            for j in range(n):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0