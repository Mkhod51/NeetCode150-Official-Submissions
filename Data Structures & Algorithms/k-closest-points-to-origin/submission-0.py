class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tupled = [(math.sqrt((0-x)**2 + ((0-y)**2)), [x,y]) for (x,y) in points]
        heapq.heapify(tupled)


        return [heapq.heappop(tupled)[1] for _ in range(k)]

