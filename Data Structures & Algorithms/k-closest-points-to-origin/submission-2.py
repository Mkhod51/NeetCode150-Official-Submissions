class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for (x,y) in points:
            keyValue = (-(x*x + y*y), [x,y])
            heapq.heappush(heap, keyValue)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [pair for dist,pair in heap]




