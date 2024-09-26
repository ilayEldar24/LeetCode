class Solution(object):
    def getConcatenation(self, nums):
        
        origLen = len(nums)
        
        for i in range(origLen):
            nums.append(nums[i])
        
        return nums
        