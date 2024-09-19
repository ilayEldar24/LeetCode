class Solution(object):
    def threeSum(self, nums):
        sortedNums = sorted(nums)
        res = set()
        
        for index, num in enumerate(sortedNums):
            if index > 0 and num == sortedNums[index-1]:
                continue
            target = 0 - num
            l , r = index + 1, len(nums) - 1
            
            while l < r:
                curSum = sortedNums[l] + sortedNums[r]
                if curSum == target:
                    res.add(tuple([num,sortedNums[l],sortedNums[r]]))
                    l+=1
                    r-=1
                elif curSum < target:
                    l +=1
                else:
                    r -=1
        return res