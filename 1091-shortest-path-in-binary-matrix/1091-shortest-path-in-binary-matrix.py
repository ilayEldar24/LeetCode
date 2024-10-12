from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        
        # Check if start or end are blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # Initialize BFS queue and visited set
        queue = deque([(0, 0)])  # Start from top-left corner
        visited = set([(0, 0)])  # Mark start as visited
        level = 1  # Distance level (first step is level 1)
        
        directions = [[-1,-1], [-1,0], [-1,1], [0,1],[1,1],[1,0],[1,-1], [0,-1]]
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                
                # Check if we've reached the bottom-right corner
                if r == n - 1 and c == n - 1:
                    return level
                
                # Explore all 8 possible directions
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    
                    # Check bounds and if the cell is valid to move to
                    if 0 <= newR < n and 0 <= newC < n and grid[newR][newC] == 0 and (newR, newC) not in visited:
                        queue.append((newR, newC))
                        visited.add((newR, newC))  # Mark as visited
            
            level += 1  # Increment distance level
        
        return -1  # No path found
