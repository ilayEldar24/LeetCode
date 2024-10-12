class Solution:
    def lastStoneWeight(self, stones):
        modified = [stone * -1 for stone in stones]

        heapq.heapify(modified)

        while len(modified) > 1:
            biggest = heapq.heappop(modified) * -1
            secBiggest = heapq.heappop(modified) * -1
            
            if biggest != secBiggest:
                toInsert = (biggest - secBiggest) * -1
                heapq.heappush(modified,toInsert)
        res = [num * -1 for num in modified]
        if res:
            return res[0]
        else:
            return 0