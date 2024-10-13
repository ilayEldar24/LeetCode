class Solution:
    def rob(self, nums) -> int:
        
        if len(nums) ==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        i = 2
        
        first = nums[0]
        second = max(nums[0],nums[1])
        
        while i < len(nums):
            if nums[i] + first > second:
                tmp = first
                first = second
                second = tmp + nums[i]
            else:
                first= second
            i+=1

        return second