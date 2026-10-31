class Solution:
    def check_box(self,board,boxes,i,j):
        
        if (i//3,j//3) in boxes:
            x,y = boxes[(i//3,j//3)]
         
            if i != x and j != y and board[x][y].isdigit() and board[i][j] == board[x][y]:
                print("here")
                return False
            if i != x and j != y + 1  and board[x][y+1].isdigit()  and board[i][j] == board[x][y+1]:
                print("here")
                return False
                
            if i != x and j != y + 2  and board[x][y+2].isdigit()  and board[i][j] == board[x][y + 2]:
                print(i//3,j//3)
                print()
                return False
            if i != x + 1 and j != y and board[x+1][y].isdigit()  and board[i][j] == board[x+1][y]:
              
                return False
            if i != x + 1 and j != y + 1 and board[x+1][y+1].isdigit()  and board[i][j] == board[x+1][y+1]:
               
                return False
            if i != x + 1 and j != y + 2 and board[x+1][y+2].isdigit()   and board[i][j] == board[x+1][y+2]:
                print(x,y)
                print(i,j)
             
                return False
            if i != x + 2 and j != y and board[x+2][y].isdigit()   and board[i][j] == board[x+2][y]:
            
          
                return False
            if i != x + 2 and j != y + 1 and board[x+2][y+1].isdigit()  and board[i][j] == board[x+2][y + 1]:
             
                return False
            if i != x  + 2 and j != y + 2  and board[x+2][y+2].isdigit() and board[i][j] == board[x+2][y + 2]:
           
                return False
      

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {(0,0):(0,0),(0,1):(0,3),(0,2):(0,6),(1,0):(3,0),(2,0):(6,0),(1,1):(3,3),(2,1):(6,3),(1,2):(3,6),(2,2):(6,6)
        }
        dup_row = defaultdict(set)
        dup_col = {}
        for i,x in enumerate(board):
            dup_col = {}
            
            
            for j,y in enumerate(board[i]):
                if board[i][j].isdigit():

                    if j in dup_row and board[i][j] in dup_row[j]:
                     
                        return False
                    if board[i][j] in dup_col:
                       
                        return False
                    dup_col[board[i][j]] = 1
                    dup_row[j].add(board[i][j])
             
                    if self.check_box(board,boxes,i,j) == False:
                        
                        return False
        return True