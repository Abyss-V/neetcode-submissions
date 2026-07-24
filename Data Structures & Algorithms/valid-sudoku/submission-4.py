class Solution:
    def isvalidbox(self,grid,x,y):
        if grid[x][y].isdigit() and not int(grid[x][y]) > 0 and not int(grid[x][y]) <= 9:
            return False
        elif  grid[x][y + 1].isdigit() and not int(grid[x][y + 1]) > 0 and not int(grid[x][y + 1]) <= 9:
            return False
        elif grid[x][y + 2].isdigit() and not int(grid[x][y + 2]) > 0 and not int(grid[x][y + 2]) <= 9:
            return False
        elif grid[x + 1][y].isdigit() and not int(grid[x + 1][y]) > 0 and not int(grid[x + 1][y]) <= 9:
            return False
        elif grid[x + 1][y + 1].isdigit() and not int(grid[x + 1][y + 1]) > 0 and not int(grid[x + 1][y + 1]) <= 9:
            return False
        elif grid[x + 1][y + 2].isdigit() and  not int(grid[x + 1][y + 2]) > 0 and not int(grid[x + 1][y + 2]) <= 9:
            return False
        elif grid[x + 2][y].isdigit() and not int(grid[x + 2][y]) > 0 and not int(grid[x + 2][y]) <= 9:
            return False
        elif grid[x + 2][y + 1].isdigit() and  not int(grid[x + 2][y + 1]) > 0 and  not int(grid[x + 2][y + 1]) <= 9:
            return False
        elif grid[x + 2][y + 2].isdigit() and  not int(grid[x + 2][y + 2]) > 0 and not int(grid[x + 2][y + 2]) <= 9:
            return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dup_row = {}
        col = 0
        for i,x in enumerate(board):
            dup_col = {}
            for j,y in enumerate(board[i]):
                if board[i][j].isdigit() and board[i][j] in dup_col:
                    return False
                elif board[i][j].isdigit():
                    dup_col[board[i][j]] = 1
        row = 0
        col = 0
        while col < 9:
            if row >= 9:
                dup_row = {}
                col += 1
                row = 0
            if col == 9:
                break
            if board[row][col].isdigit() and board[row][col] in dup_row:
                    return False
            elif board[row][col].isdigit():
                    dup_row[board[row][col]] = 1
            row += 1
        dup = {}
        for i,x in enumerate(board):
            for j,y in enumerate(board[i]):
                if board[i][j].isdigit() and (int(i/3),int(j/3),board[i][j]) in dup:
                    return False
                if board[i][j].isdigit():
                    dup[(int(i/3),int(j/3),board[i][j])] = 1
    
        return True
                
                