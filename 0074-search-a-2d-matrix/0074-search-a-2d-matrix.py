class Solution(object):
    def searchMatrix(self, matrix, target):
        
        l = 0 
        m,n = len(matrix), len(matrix[0])
        r = m*n - 1
        
        while l <= r:
            mid = (l+r) //2
            i = mid // n
            j = mid % n
            if matrix[i][j] == target:
                return True
            else:
                if matrix[i][j] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False

   