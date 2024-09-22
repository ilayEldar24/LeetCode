class Solution(object):
    def removeElement(self, nums, val):
        def swap(arr, l, r):
            tmp = arr[l]
            arr[l] = arr[r]
            arr[r] = tmp

        l = 0
        r = len(nums) - 1
        while (l < r):
            if nums[l] == val:
                if nums[r] != val:
                    swap(nums, l, r)
                    r -= 1
                    l += 1
                elif nums[r] == val:
                    r -= 1
            else:
                l += 1
                
        for i in range(len(nums)):
            if nums[i] == val:
                nums = nums[:i]
                return i
