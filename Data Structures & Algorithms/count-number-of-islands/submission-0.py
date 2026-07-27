class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        islands = 0
        def bfs(i,j):
            grid[i][j] = "0"
            q = deque([(i,j)])
            visited = set()
            while q:
                k,l= q.popleft()
                for dr,dc in directions:
                    if k+dr >= len(grid) or k+dr < 0 or l+dc >= len(grid[0]) or l+dc < 0 or grid[k+dr][l+dc] == "0" or (k+dr,l+dc) in visited:
                        continue
                    grid[k+dr][l+dc] = "0"
                    visited.add((k+dr,l+dc))
                    q.append((k+dr,l+dc))
                    
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if grid[i][j] == "1":
                    bfs(i,j)
                    islands += 1
        return islands