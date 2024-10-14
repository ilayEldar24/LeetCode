class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ROWS, COLS = m, n
        
        prev = [0]*COLS
        
        for i in range(ROWS):
            cur = [0]*COLS
            cur[-1] = 1
            for j in range(COLS-2,-1, -1):
                cur[j] = cur[j+1] + prev[j]
            prev = cur
        
        return cur[0]
    