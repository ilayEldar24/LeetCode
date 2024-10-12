class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == "2" or grid[r][c] == "0":
                return
            
            grid[r][c] = "2"
            
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r+1,c)
            dfs(r,c+1)
        
        
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r,c)
                c += 1
            r+= 1
        
        return res
        
        
        
            
            
            
            
            
        