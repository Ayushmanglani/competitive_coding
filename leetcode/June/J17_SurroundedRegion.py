def floodFill(board,x,y):
    if (x < 0 or x >= M or y < 0 or y >= N):
        return
    if (board[x][y] != pre): 
        return
    
    board[x][y] = new
  
    floodFill(board, x+1, y) 
    floodFill(board, x-1, y) 
    floodFill(board, x, y+1) 
    floodFill(board, x, y-1)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if board:
            global M,N,pre,new
            pre = '-'
            new = 'O'
            M = len(board)
            N = len(board[0])
            
            for i in range(M):
                for j in range(N):
                    if board[i][j] == 'O':
                        board[i][j] = '-'
            
            for i in range(M):
                if (board[i][0] == '-'):
                    floodFill(board, i, 0) 
            for i in range(M):
                if (board[i][N-1] == '-'): 
                    floodFill(board, i, N-1)
            for i in range(1,N-1):
                if (board[0][i] == '-'):
                    floodFill(board, 0, i)
            for i in range(1,N-1):
                if (board[M-1][i] == '-'):
                    floodFill(board, M-1, i)
                    
            for i in range(1,M-1):
                for j in range(1,N-1):
                    if board[i][j] == '-':
                        board[i][j] = 'X'
                        
        return board