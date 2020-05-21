class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        m = len(matrix)
        n = len(matrix[0])
        count += sum(matrix[i][n-1] for i in range(m))
        count += sum(matrix[m-1][i] for i in range(n))
        count -= matrix[m-1][n-1]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i+1][j+1],matrix[i] [j+1],matrix[i+1][j])+1
                else:
                    matrix[i][j] = 0
                count += matrix[i][j]
        return(count)