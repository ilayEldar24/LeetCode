import math
import heapq

class Solution:
    def kClosest(self, points, k):
        def calcDist(point):
            return math.sqrt(point[0]**2 + point[1]**2)
        
        res = []
        modified = [(calcDist(point), point) for point in points]
        heapq.heapify(modified)

        for i in range(k):
            res.append(heapq.heappop(modified)[1])
        
        return res






        
        
        