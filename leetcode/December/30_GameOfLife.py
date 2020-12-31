class Solution(object):
    def gameOfLife(self, board):
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        rows = len(board)
        cols = len(board[0])

        # Create a copy of the original board
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        # Iterate through board cell by cell.
        for row in range(rows):
            for col in range(cols):

                # For each cell count the number of live neighbors.
                live_neighbors = 0
                for neighbor in neighbors:

                    r = (row + neighbor[0])
                    c = (col + neighbor[1])

                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    # The evaluation is done against the copy, since that is never updated.
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3        
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1


class Solution(object):
    def gameOfLife(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = 0
                direction = [(-1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]
                for a, b in direction:
                    if 0<= i+a < len(board) and 0<= j+b < len(board[0]) and abs(board[i+a][j+b]) == 1:
                        res += 1
                if board[i][j] == 1 and (res <2 or res>3):
                    board[i][j] = -1
                if board[i][j] == 0 and res ==3:
                    board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] ==2:
                    board[i][j] = 1
                if board[i][j] == -1:
                    board[i][j] = 0                    