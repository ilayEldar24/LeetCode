class Solution(object):
    def search(self, nums, target):
        
        pivot = findPivot(nums)
        size = len(nums)
        
        l = 0
        r = len(nums)
        
        while l <= r: 
            mid = (l+r) // 2
            logicMid = logicInd(mid, pivot, size)
            if nums[logicMid] == target:
                return logicMid
            if nums[logicMid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        
             
def logicInd(ind, pivot, size):
    return  (ind+pivot) % size



def findPivot(nums):
    pivot = 0
    for index, num in enumerate(nums[:-1]):
        if num > nums[index+1]:
            pivot = index+1
            break
    return pivot
