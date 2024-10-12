from collections import deque
class Solution:
    def orangesRotting(self, grid):
        
        ROWS, COLS = len(grid), len(grid[0])
        totalAmount, rottenAmount = 0, 0
        
        queue = deque()
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    totalAmount += 1
                elif grid[r][c] == 2:
                    totalAmount +=1
                    rottenAmount +=1
                    queue.append([r,c])
        
        time = 0
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        if totalAmount == rottenAmount:
                return time
        
        while queue:
            if totalAmount == rottenAmount:
                return time
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    if min(r+dr, c+dc) < 0 or r + dr == ROWS or c + dc == COLS or grid[r+dr][c+dc] == 0 or grid[r+dr][c+dc] == 2:
                        continue
                    else:
                        grid[r+dr][c+dc] = 2
                        queue.append([r+dr,c+dc])
                        rottenAmount += 1
            time += 1
        return -1
                    
                