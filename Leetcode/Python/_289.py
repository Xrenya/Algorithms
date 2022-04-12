class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        row_len = len(board)
        col_len = len(board[0])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                live_neighbours = 0
                for neighbour in neighbours:
                    
                    row = i + neighbour[0]
                    col = j + neighbour[1]
                    
                    if (row > -1 and row < row_len) and (col > -1 and col < col_len) and abs(board[row][col]) == 1:
                        live_neighbours += 1

                if (live_neighbours < 2 or live_neighbours > 3) and abs(board[i][j]) == 1:
                    board[i][j] = -1 # was alive -> now dead

                    
                elif live_neighbours == 3 and board[i][j] == 0:
                    board[i][j] = 2 # was dead -> now alive

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 0 if board[i][j] == 0 or board[i][j] == -1 else 1
        
