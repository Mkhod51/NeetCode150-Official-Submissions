class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [((d[0] ** 2) + (d[1] ** 2), [d[0], d[1]]) for d in points]
        print(dists)
        heapq.heapify(dists) 
        res = []

        while k > 0:
            dist, point = heapq.heappop(dists)

            res.append(point)
            k-=1
        
        return res 