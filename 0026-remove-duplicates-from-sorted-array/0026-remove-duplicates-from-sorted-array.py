class Solution(object):
    def removeDuplicates(self , nums):
        l=r=1
        size = len(nums)
        
        while r < size :
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            r += 1
            
        return l 