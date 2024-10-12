class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = {}
        
        for num in nums:
            if num in hset:
                return True
            else:
                hset[num] = 1
            
        return False
                
        