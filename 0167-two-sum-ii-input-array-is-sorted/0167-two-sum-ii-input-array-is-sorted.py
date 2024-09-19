class Solution(object):
    def twoSum(self, numbers, target):
        l,r = 0,len(numbers)-1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [l+1,r+1]
            elif curSum > target:
                r -= 1
            else:
                l += 1
            
        
        