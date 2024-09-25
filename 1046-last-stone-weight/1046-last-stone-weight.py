
class Solution(object):
    def lastStoneWeight(self, stones):
        
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            num1 = heapq.heappop(stones) * -1
            num2 = heapq.heappop(stones) * -1
            
            if num1!=num2:
                newNum = num2-num1
                heapq.heappush(stones, newNum)
        if stones:
            return stones[0]*-1
        else:
            return 0
            