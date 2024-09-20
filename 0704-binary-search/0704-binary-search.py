class Solution(object):
    def search(self, nums, target):
        def helper(nums,l,r,target):
            if l > r:
                return -1
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if  nums[mid] > target:
                return helper(nums,l,mid-1,target)
            else:
                return helper(nums,mid+1,r,target)
        return helper(nums,0,len(nums)-1,target)

