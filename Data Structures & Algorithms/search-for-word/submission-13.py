class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        valid = False
     
        path = set()
        def dfs(k,i,j):
            if k == len(word):
                return True
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or (i,j) in path or board[i][j] != word[k]:
                return False
            
            path.add((i,j))
            res = dfs(k + 1,i+1,j) or dfs(k + 1,i,j+1) or dfs(k + 1,i-1,j) or dfs(k + 1,i,j-1)
            path.remove((i,j))
            print(res)
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0,i,j):
                    return True
        return False
 
            
            
