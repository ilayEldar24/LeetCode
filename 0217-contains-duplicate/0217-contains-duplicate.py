from collections import defaultdict


class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()

        for num in nums:
            if num in hset:
                return True
            else:
                hset.add(num)
        return False
