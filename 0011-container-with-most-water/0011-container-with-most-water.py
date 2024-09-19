class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        maxAmount=0
        
        while l < r:
            cur_width = r - l
            cur_height = min(height[l], height[r])
            curAmount = cur_width * cur_height
            if curAmount > maxAmount:
                maxAmount = curAmount
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        
        return maxAmount
            
            
        