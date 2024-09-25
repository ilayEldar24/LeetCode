import heapq

class Solution(object):
    def kClosest(self, points, k):
        heap = [(((point[0])**2 + (point[1]**2))**0.5, [point[0],point[1]]) for point in points]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
 