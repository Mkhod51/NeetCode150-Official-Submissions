"""
k=4
1,2,3,4,4,55,6,7,8,9,10
4th largest is 6th smallest 
"""


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k 

        for n in nums:
            heapq.heappush(self.heap, n)

            if len(self.heap) > k:
                heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
