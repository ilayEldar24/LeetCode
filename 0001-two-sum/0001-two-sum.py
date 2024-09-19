class Solution(object):
    def twoSum(self, nums, target):
        hmap = {}

        for index, num in enumerate(nums):
            wanted = target - num

            if hmap.get(wanted, -1) != -1:
                return(index, hmap[wanted])
            
            hmap[num] = index

    

            

        