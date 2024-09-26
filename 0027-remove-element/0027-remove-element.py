
class Solution(object):
    def removeElement(self, nums, val):
        l , r = 0, len(nums) - 1
        
        if not nums:
            return 0
        
        while l < r:
            if nums[r] == val:
                    r-=1
            else:
                if nums[l] == val:
                    tmp = nums[l]
                    nums[l] = nums[r]
                    nums[r] = tmp
                    r-=1
                l+=1
        
        if nums[l] == val:
            return l
        else:
            return l+1