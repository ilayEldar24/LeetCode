import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mod = [num* -1 for num in nums]
        heapq.heapify(mod)
        
        for i in range(k):
            cur = heapq.heappop(mod) 
        
        return cur * -1
        
        