class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None

        rowStart = 0
        rowEnd = len(matrix)
        colStart = 0
        colEnd = len(matrix[0])

        resLength = rowEnd * colEnd
        res = []
        dir = 0
        while len(res) < resLength:
            if dir == 0: #Right
                for i in range(colStart,colEnd):
                    res.append(matrix[rowStart][i])
                rowStart += 1
            elif dir == 1: #Down
                for i in range(rowStart,rowEnd):
                    res.append(matrix[i][colEnd-1])
                colEnd -= 1
            elif dir == 2: #Left
                for i in range(colEnd-1,colStart-1,-1):
                    res.append(matrix[rowEnd-1][i])
                rowEnd -= 1
            elif dir == 3: #Up
                for i in range(rowEnd-1,rowStart-1,-1):
                    res.append(matrix[i][colStart])
                colStart += 1
            dir = (dir+1)%4 
        return res