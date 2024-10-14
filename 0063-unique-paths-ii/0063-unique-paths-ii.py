class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        
        prev = [0]*COLS
               
        for i in range(ROWS-1, -1, -1):
            cur = [0]*COLS
            for j in range(COLS-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                else:
                    if i == ROWS - 1 and j == COLS - 1:
                        cur[j] = 1
                    else:
                        if j == COLS -1:
                            cur[j] = prev[j]
                        else:
                            cur[j] = cur[j+1] + prev[j]
            prev = cur
        
        return cur[0]
        
        return cur[0]